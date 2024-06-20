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
    return root_node, code
