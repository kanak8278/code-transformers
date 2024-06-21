import py_compile
from argparse import ArgumentParser

def compile_file(file_path):
    try:
        py_compile.compile(file_path, doraise=True)
        return True, f"Compilation of {file_path} succeeded."
    except py_compile.PyCompileError as e:
        return False, f"Compilation of {file_path} failed: {e.msg}"
    except Exception as e:
        return False, f"An unexpected error occurred during the compilation of {file_path}: {str(e)}"


if __name__ == "__main__":
    # Create an argument parser
    parser = ArgumentParser(description="Compile a Python file.")
    # Add the file argument
    parser.add_argument("--file", "-f", help="Python file to compile")
    # Parse the arguments
    args = parser.parse_args()
    # Compile the file
    print(compile_file(args.file))
