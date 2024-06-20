from utils.analyzer import analyze_repo
from utils.modifier import modify_caller, modify_callee

def main(repo_path, instruction1, instruction2):
    functions, calls = analyze_repo(repo_path)

    print("Functions found in the repository:")
    for function_name, function in functions.items():
        print(
            f"Function: {function_name}, File: {function['file_path']}, Parameters: {function['parameters']}, Start: {function['start_point']}, End: {function['end_point']}"
        )

    print("\nFunction calls found in the repository:")
    for call in calls:
        print(
            f"Function call: {call[0]}, File: {call[1]}, Start: {call[2]}, End: {call[3]}"
        )

    modify_caller(instruction1, "factorial", functions)
    modify_callee(instruction2, "factorial", functions, calls)

if __name__ == "__main__":
    instruction1 = """
You are given a simple recursive function that calculates the factorial of a number. Enhance this function to use memoization to cache previously calculated results. Follow the steps below to achieve this.

Define a global dictionary factorial_cache to store the cached results.
Modify the factorial function to check if the result for n is already in the cache. If so, return the cached result.
If n is 0, return 1 (base case).
If the result is not cached, compute the factorial recursively and store the result in the cache before returning it.
"""
    instruction2 = """
Modify the function invocation. 
"""

    main("factorial", instruction1, instruction2)
