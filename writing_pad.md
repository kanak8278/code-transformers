1. Places which use external variable are difficult to handle.
factorial_cache = {}
```python
def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    factorial_cache[n] = result
    return result
```

# Structural Comparison of Python Files:
1. **AST to Structure Conversion**:
   The AST (Abstract Syntax Tree) of each Python file is converted into a structured, comparable format. This structure includes node types, fields, attributes, and their depth in the tree, preserving the hierarchical nature of the AST.

2. **String Representation**:
   The structured AST is converted into a string representation to facilitate comparison using `difflib`. This allows for a line-by-line textual comparison.

3. **Detailed Diff Generation**:
   `difflib.unified_diff` generates a detailed unified diff, showing exactly where the structures differ. This provides a clear, visual representation of differences.

4. **Similarity Ratio Calculation**:
   `difflib.SequenceMatcher` calculates a similarity ratio between the string representations. This ratio provides a numeric score representing the similarity of the two AST structures.

### Advantages Over Using `AST` Alone

1. **Detailed Differences**:
   The combined approach offers a detailed diff output, showing specific differences in the structure of the two files. Using `ast` alone typically provides only a binary match/mismatch without details.

2. **Quantitative Similarity Score**:
   The similarity ratio offers a numeric metric to quantify the degree of similarity between the files. This helps measure how close the generated file is to the ground truth.

3. **Preserved Structure**:
   By including indentation and hierarchy in the structured format, the comparison considers the full structure of the code, including nested relationships. This detailed insight is more informative than a simple structural comparison.

4. **Flexibility and Insight**:
   Combining AST analysis with `difflib`'s text comparison tools provides both structural insight and textual differences. This dual perspective makes it easier to understand and debug the differences, offering both high-level and low-level views.


###  `diff` Metric Implementation

1. **Remove Comments and Docstrings**:
   Focuses on comparing the actual code logic by removing comments and docstrings, ensuring that only functional code differences are highlighted.

2. **Generate Unified Diff**:
   Provides a detailed, line-by-line comparison of the code, making it clear where and how the files differ.

3. **Calculate Similarity Ratio**:
   Produces a numeric score representing the similarity between the two files, helping to quantify the extent of differences.

### Benefits

- **Clarity**: Highlights functional differences, ignoring non-essential comments and docstrings.
- **Detail**: Offers precise insight into specific changes.
- **Quantification**: The similarity ratio gives a clear measure of how alike the two files are, useful for evaluating changes.


# Other Metrics
1. Semantic similarity: Use embeddings from models like CodeBERT or GPT-4 to measure the semantic similarity of code snippets.
