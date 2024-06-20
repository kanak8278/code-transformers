from utils.analyzer import analyze_repo
from utils.modifier import modify_caller, modify_callee
import os

def main(repo_path, function_name, instruction1, instruction2):
    functions, calls = analyze_repo(repo_path)

    print("Functions found in the repository:")
    for function_name, function in functions.items():
        print(
            f"Function: {function_name}, File: {function['file_path']}, Parameters: {function['parameters']}, Start: {function['start_point']}, End: {function['end_point']}"
        )

    print("\nFunction calls found in the repository:")
    for call in calls:
        print(
            f'Function call: {call["function_name"]}, File: {call["file_path"]}, Start: {call["call_start"]}, End: {call["call_end"]}'
        )

    modify_caller(instruction1, function_name, functions)
    modify_callee(instruction2, function_name, functions, calls)

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

#     instruction1 = """
# You are given a simple recursive function that calculates the factorial of a number. Enhance this function to use memoization to cache previously calculated results. Follow the steps below to achieve this.

# Define a global dictionary factorial_cache to store the cached results.
# Modify the factorial function to check if the result for n is already in the cache. If so, return the cached result.
# If n is 0, return 1 (base case).
# If the result is not cached, compute the factorial recursively and store the result in the cache before returning it.
# """
#     instruction2 = """
# Modify the function invocation. 
# """`

    main(repo_path, function_name, instruction1, instruction2)
