import ast
import difflib

def ast_to_structure(node, depth=0):
    """Convert an AST node to a comparable structure, preserving indentation."""
    if not isinstance(node, ast.AST):
        return node
    fields = [(name, ast_to_structure(value, depth + 1)) for name, value in ast.iter_fields(node)]
    attributes = [(name, ast_to_structure(getattr(node, name), depth + 1)) for name in node._attributes]
    return (node.__class__.__name__, fields, attributes, depth)

def get_ast_structure(file):
    """Parse a Python file and return its AST structure."""
    with open(file, "r") as f:
        tree = ast.parse(f.read(), filename=file)
    return ast_to_structure(tree)

def compare_ast(file1, file2):
    """Compare the AST structures of two files and return a diff and similarity score."""
    structure1 = get_ast_structure(file1)
    structure2 = get_ast_structure(file2)
    
    structure1_str = str(structure1)
    structure2_str = str(structure2)
    
    diff = list(difflib.unified_diff(structure1_str.splitlines(), structure2_str.splitlines(), lineterm=''))
    
    sm = difflib.SequenceMatcher(None, structure1_str, structure2_str)
    similarity_ratio = sm.ratio()

    
    return diff, similarity_ratio
if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Compare two Python files.")
    # Add the file arguments
    parser.add_argument("--file1", "-f1", type=str, help="Path to the first file.")
    parser.add_argument("--file2", "-f2", type=str, help="Path to the second file.")
    args = parser.parse_args()
    result = compare_ast(args.file1, args.file2)

    print(result)
