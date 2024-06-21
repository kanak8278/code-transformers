from utils.analyzer import analyze_repo
from utils.modifier import modify_caller, modify_callee
import os

def main(repo_path, func_name, instruction1, instruction2):
    functions, calls = analyze_repo(repo_path)

    print("Functions found in the repository:")
    for name, function in functions.items():
        print(
            f"Function: {name}, File: {function['file_path']}, Parameters: {function['parameters']}, Start: {function['start_point']}, End: {function['end_point']}"
        )

    print("\nFunction calls found in the repository:")
    for call in calls:
        print(
            f'Function call: {call["function_name"]}, File: {call["file_path"]}, Start: {call["call_start"]}, End: {call["call_end"]}'
        )

    modify_caller(instruction1, func_name, functions)
    modify_callee(instruction2, func_name, functions, calls)

if __name__ == "__main__":

    # read everything from the arguments ArgumentParser
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("--repo_path", type=str, required=True)
    parser.add_argument("--function_name", type=str, required=True)
    parser.add_argument("--instruction1", type=str, required=True)
    parser.add_argument("--instruction2", type=str, required=True)
    args = parser.parse_args()

    if args.repo_path and os.path.exists(args.repo_path):
        repo_path = args.repo_path
    else:
        raise ValueError("Invalid repo path")
    if args.function_name:
        function_name = args.function_name

    if args.instruction1:
        # instruction1 is file path
        with open(args.instruction1, "r") as file:
            instruction1 = file.read()
    else:
        instruction1 = args.instruction1
    
    if args.instruction2:
        # instruction2 is file path
        with open(args.instruction2, "r") as file:
            instruction2 = file.read()
    else:
        instruction2 = args.instruction2
    
    if args.function_name:
        function_name = args.function_name
    
    # print repo_path and func name at different places
    print("Repo:", repo_path)
    print("Function Name:", function_name)
    print()
    main(repo_path, function_name, instruction1, instruction2)
