#!/bin/bash

# Folder name passed as the first argument
folder=$1

# Check if the folder exists in the current working directory
if [ -d "$folder" ]; then
    # If the folder exists, run the commands
    python main.py --repo_path "$folder" --function_name "$folder" --instruction1 "$folder/instruction1.txt" --instruction2 "$folder/instruction2.txt"
    python -m tests.test_"$folder"
    python metrics/diff.py --file1 "$folder/helper.py" --file2 "ground_truth/$folder.py"
    python metrics/structural_comparison.py --file1 "$folder/helper.py" --file2 "ground_truth/$folder.py"
    python metrics/compiler.py --file "$folder/new_helper.py"
    python metrics/compiler.py --file "$folder/new_call.py"
else
    # If the folder does not exist, print an error message
    echo "Error: Folder '$folder' does not exist in the current working directory"
fi