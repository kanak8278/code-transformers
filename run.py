import os
from metrics.compiler import compile_file
from metrics.diff import compare_files
from metrics.structural_comparison import compare_ast
from utils.analyzer import analyze_repo
from utils.modifier import modify_caller, modify_callee
from tests.test_greeting import run_tests as run_greeting_tests
from tests.test_factorial import run_tests as run_factorial_tests
from tests.test_square_sum import run_tests as run_square_sum_tests


if __name__ == "__main__":
    results = []
    for folder in os.listdir("examples"):
        repo_path = os.path.join("examples", folder)
        functions, calls = analyze_repo(repo_path)
        print("Functions found in the repository:")
        for name, function in functions.items():
            print(
                f"Function: {name}, File: {function['file_path']}, Parameters: {function['parameters']}, Start: {function['start_point']}, End: {function['end_point']}"
            )

        print("\nFunction calls found in the repository:")
        for call in calls:
            print(
                f'Function call: {call["function_name"]}, File: {call["file_path"]}, Start: {call["call_start"]}, End: {call["call_end"]}'
            )
        instruction1_path = os.path.join("examples", folder, "instruction1.txt")
        instruction2_path = os.path.join("examples", folder, "instruction2.txt")
        with open(instruction1_path, "r") as file:
            instruction1 = file.read()
        with open(instruction2_path, "r") as file:
            instruction2 = file.read()
        
        modify_caller(instruction1, folder, functions)
        modify_callee(instruction2, folder, functions, calls)
        
        gold = os.path.join("ground_truth", f"{folder}.py")
        helper_modified = os.path.join("examples", folder, "new_helper.py")
        call_modified = os.path.join("examples", folder, "new_call.py")
        
        with open(gold, "r") as file:
            gold_code = file.read()
        with open(helper_modified, "r") as file:
            modified_code = file.read()
        

        diff, similarity, bleu_score = compare_files(gold_code, modified_code)

        is_call_error, call_desc = compile_file(call_modified)
        is_helper_error, call_helper = compile_file(helper_modified)

        

        print("Diff: ", diff)
        print(f"\nSimilarity ratio: {similarity:.2f}")
        print(f"\nBLEU score: {bleu_score:.2f}")
        print(f"\nCompile Error for modified call: {is_call_error}")
        print(f"\nCompile Error for modified helper: {is_helper_error}")
        print("=============================================================")
        print("\n\n")

        if folder == "greeting":
            result = run_greeting_tests()
        elif folder == "factorial":
            result = run_factorial_tests()
        elif folder == "sum_of_squares":
            result = run_square_sum_tests()
    
        results.append({
            "folder": folder,
            # "diff": "\n".join(diff),
            "similarity": similarity,
            "bleu_score": bleu_score,
            "is_call_error": is_call_error,
            "is_helper_error": is_helper_error,
            "call_desc": call_desc,
            "call_helper": call_helper,
            "test_passed": result.success_count
        })
    # convert result json into csv file using pandas
    import pandas as pd
    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)
    