## Structural Comparison of Python Files:
1. **AST to Structure Conversion**:
   The AST (Abstract Syntax Tree) of each Python file is converted into a structured, comparable format. This structure includes node types, fields, attributes, and their depth in the tree, preserving the hierarchical nature of the AST.

2. **String Representation**:
   The structured AST is converted into a string representation to facilitate comparison using `difflib`. This allows for a line-by-line textual comparison.

3. **Detailed Diff Generation**:
   `difflib.unified_diff` generates a detailed unified diff, showing exactly where the structures differ. This provides a clear, visual representation of differences.

4. **Similarity Ratio Calculation**:
   `difflib.SequenceMatcher` calculates a similarity ratio between the string representations. This ratio provides a numeric score representing the similarity of the two AST structures.


##  `diff` Metric Implementation
1. **Remove Comments and Docstrings**:
   Focuses on comparing the actual code logic by removing comments and docstrings, ensuring that only functional code differences are highlighted.

2. **Generate Unified Diff**:
   Provides a detailed, line-by-line comparison of the code, making it clear where and how the files differ.

3. **Calculate Similarity Ratio**:
   Produces a numeric score representing the similarity between the two files, helping to quantify the extent of differences.
4. **Diff based Bleu Score**:
   The diff based Bleu score is calculated by comparing the diff of the two files and calculating the Bleu score based on the diff. This helps in understanding the similarity between the two files based on the diff.


## Code Compilation
Used `py_compile` to compile the code and check for syntax errors. This is done to ensure that the code is syntactically correct and can be executed without errors.

## Unit tests & Code Execution
Run the unit tests on the modified functions to ensure that the changes do not affect the functionality. The modified functions are executed to generate the output files and check for any runtime errors. 

