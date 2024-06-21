import difflib
import ast
import re
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def remove_comments_and_docstrings(source):
    """Remove comments and docstrings from the source code, preserving indentation."""
    def remove_comments(line):
        """Remove comments from a single line."""
        return re.sub(r'#.*', '', line)

    def visit_node(node, lines):
        """Visit each node and filter out docstrings."""
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Str):
                docstring_node = node.body[0]
                docstring_start_line = docstring_node.lineno - 1
                docstring_end_line = docstring_node.end_lineno - 1
                for i in range(docstring_start_line, docstring_end_line + 1):
                    lines[i] = ''

        for child in ast.iter_child_nodes(node):
            visit_node(child, lines)

    tree = ast.parse(source)
    lines = source.splitlines()
    visit_node(tree, lines)

    # Remove comments from each line
    lines = [remove_comments(line) for line in lines]
    
    return "\n".join(lines)

def tokenize_code(source):
    """Tokenize the source code into a list of tokens."""
    return re.findall(r'\w+|\S', source)

def compare_files(content1, content2):
    
    # Remove comments and docstrings
    clean_content1 = remove_comments_and_docstrings(content1)
    clean_content2 = remove_comments_and_docstrings(content2)
    
    # Split the clean content into lines
    lines1 = clean_content1.splitlines()
    lines2 = clean_content2.splitlines()
    
    # Get the unified diff
    diff = difflib.unified_diff(lines1, lines2, lineterm='')
    diff_list = list(diff)
    
    # Calculate the similarity ratio
    sm = difflib.SequenceMatcher(None, lines1, lines2)
    similarity_ratio = sm.ratio()

    # Tokenize the cleaned content
    tokens1 = tokenize_code(clean_content1)
    tokens2 = tokenize_code(clean_content2)

    # Calculate BLEU score with smoothing function
    chencherry = SmoothingFunction()
    bleu_score = sentence_bleu([tokens1], tokens2, smoothing_function=chencherry.method1)
    
    
    return diff_list, similarity_ratio, bleu_score

# Example usage
if __name__ == "__main__":
    from argparse import ArgumentParser
    # Create an argument parser
    parser = ArgumentParser(description="Compare two Python files.")
    # Add the file arguments
    parser.add_argument("--file1", "-f1", help="First Python file")
    parser.add_argument("--file2", "-f2", help="Second Python file")
    # Parse the arguments
    args = parser.parse_args()
    
    # Compare the files
    with open(args.file1, "r") as f1, open(args.file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

    diff, similarity, bleu_score = compare_files(content1, content2)

    print("\n".join(diff))
    print(f"\nSimilarity ratio: {similarity:.2f}")
    print(f"\nBLEU Score: {bleu_score:.2f}")