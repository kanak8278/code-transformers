import os
from tree_sitter import Language, Parser
import tree_sitter_python as tspython


PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)


# Function to parse the content of a file
def parse_code(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    tree = parser.parse(bytes(code, "utf8"))
    root_node = tree.root_node
    return root_node


# Function to find all function definitions
def find_functions(node, functions):
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
        functions.append((function_name, parameters, node.start_point, node.end_point))
    for child in node.children:
        find_functions(child, functions)


# Function to find all function calls
def find_function_calls(node, calls, file_path):
    if node.type == "call":
        function_name = None
        for child in node.children:
            if child.type == "identifier":
                function_name = child.text.decode("utf8")
        if function_name:
            calls.append((function_name, file_path, node.start_point, node.end_point))
    for child in node.children:
        find_function_calls(child, calls, file_path)


# Parse and find functions and calls in a file
def analyze_file(file_path):
    root_node = parse_code(file_path)
    functions = []
    calls = []
    find_functions(root_node, functions)
    find_function_calls(root_node, calls, file_path)
    return functions, calls


# Recursively check all Python files in the directory
def analyze_repo(repo_path):
    functions = []
    calls = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_functions, file_calls = analyze_file(file_path)
                functions.extend(file_functions)
                calls.extend(file_calls)
    return functions, calls


# Main function to analyze the repo and print the results
def main():
    repo_path = "example_repo"  # Change this to the path of the repository
    functions, calls = analyze_repo(repo_path)

    print("Functions found in the repository:")
    for function in functions:
        print(
            f"Function: {function[0]}, Parameters: {function[1]}, Start: {function[2]}, End: {function[3]}"
        )

    print("\nFunction calls found in the repository:")
    for call in calls:
        print(
            f"Function call: {call[0]}, File: {call[1]}, Start: {call[2]}, End: {call[3]}"
        )


if __name__ == "__main__":
    main()
