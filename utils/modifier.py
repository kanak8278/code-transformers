import os
from .llm import chat_completion_request
import json
# get current folder path
folder = os.path.dirname(os.path.abspath(__file__))
# get the prompt path which is relative prompts/system.txt
prompt_path = os.path.join(folder, "prompts")
prompt1_path = os.path.join(prompt_path, "prompt1.txt")
prompt2_path = os.path.join(prompt_path, "prompt2.txt")
with open(prompt1_path, "r") as file:
    prompt1 = file.read()

with open(prompt2_path, "r") as file:
    prompt2 = file.read()





# Function to use an LLM to modify function definitions and calls
def modify_caller(instruction, func_name, functions):
    for function_name, function in functions.items():
        if function_name == func_name:
            # Modify the function definition
            file_path = function["file_path"]
            # get folder from file_path
            folder = os.path.dirname(file_path)
            start_line, start_col = function["start_point"]
            end_line, end_col = function["end_point"]

            with open(file_path, "r") as file:
                lines = file.readlines()
            original_code = "".join(lines[start_line : end_line + 1])
            
            message = [
                {
                    "role": "system",
                    "content": prompt1.format(old_function=original_code, instruction=instruction),
                },
            ]
            output = chat_completion_request(message)
            modified_code = output.choices[0].message.content
            modified_code = modified_code.split("```python")[1].split("```")[0]
            print(modified_code)
            print()
            function[func_name] = modified_code
            
            
            folder = os.path.dirname(file_path)
            file_name = os.path.basename(file_path)
            new_file_path = os.path.join(folder, f"new_{file_name}")
            with open(new_file_path, "w") as file:
                file.write("".join(modified_code))
            


def modify_callee(instruction, func_name, functions, calls):
    for call in calls:
        if call["function_name"] == func_name:
            # Modify the function call
            function_definition = functions.get(call["function_name"])
            if not function_definition:
                continue
            
            file_path = call["file_path"]
            start_line, start_col = call["call_start"]
            end_line, end_col = call["call_end"]
            parent_function = call["parent_function"]
            parent_start = call["parent_start"]
            parent_end = call["parent_end"]

            with open(file_path, "r") as file:
                lines = file.readlines()

            original_code = lines
            message = [
                {
                    "role": "system",
                    "content": prompt2.format(older_function_invocation=original_code, new_function_definition=function_definition, instruction=instruction)
                },
            ]
            output = chat_completion_request(message)
            modified_code = output.choices[0].message.content
            modified_code = modified_code.split("```python")[1].split("```")[0]
            if isinstance(modified_code, list):
                modified_code = "".join(modified_code)
            print(modified_code)

            folder = os.path.dirname(file_path)
            file_name = os.path.basename(file_path)
            new_file_path = os.path.join(folder, f"new_{file_name}")
            with open(new_file_path, "w") as file:
                file.write("".join(modified_code))