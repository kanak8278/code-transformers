import os
from .parser_utils import parse_code

# Function to find all function definitions
def find_functions(node, functions, file_path):
    if node.type == "function_definition":
        function_name = None
        parameters = []
        for child in node.children:
            if child.type == "identifier":
                function_name = child.text.decode("utf8")
            elif child.type == "parameters":
                parameters = [
                    param.text.decode("utf8")
                    for param in child.children
                    if param.type == "identifier"
                ]
        functions[function_name] = {
            "file_path": file_path,
            "parameters": parameters,
            "start_point": node.start_point,
            "end_point": node.end_point,
        }
    for child in node.children:
        find_functions(child, functions, file_path)

# Function to find all function calls
def find_function_calls(node, calls, file_path, functions):
    if node.type == "call":
        function_name = None
        parent_function = None
        parent_start = None
        parent_end = None

        for child in node.children:
            if child.type == "identifier":
                function_name = child.text.decode("utf8")

        if function_name:
            call_start, call_end = node.start_point, node.end_point
            is_within_own_function = False

            # Check if the call is within its own function definition
            for func_name, func_info in functions.items():
                if func_info['file_path'] == file_path and \
                   func_info['start_point'] <= call_start <= func_info['end_point']:
                    if func_name == function_name:
                        is_within_own_function = True
                        break

            if not is_within_own_function:
                # Check if the call is within any other function definition
                for func_name, func_info in functions.items():
                    if func_info['file_path'] == file_path and \
                       func_info['start_point'] <= call_start <= func_info['end_point']:
                        parent_function = func_name
                        parent_start = func_info['start_point']
                        parent_end = func_info['end_point']
                        break

                calls.append({
                    "function_name": function_name,
                    "file_path": file_path,
                    "call_start": call_start,
                    "call_end": call_end,
                    "parent_function": parent_function,
                    "parent_start": parent_start,
                    "parent_end": parent_end
                })

    for child in node.children:
        find_function_calls(child, calls, file_path, functions)

# Parse and find functions and calls in a file
def analyze_file(file_path):
    root_node, code = parse_code(file_path)
    functions = {}
    calls = []
    find_functions(root_node, functions, file_path)
    find_function_calls(root_node, calls, file_path, functions)

    return functions, calls, code

# Recursively check all Python files in the directory
def analyze_repo(repo_path):
    functions = {}
    calls = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_functions, file_calls, code = analyze_file(file_path)
                functions.update(file_functions)
                calls.extend(file_calls)
    return functions, calls
