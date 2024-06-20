# check if the input string is "factorial" then run the below
if [ "$1" == "factorial" ]; then
    python main.py --repo_path factorial --function_name factorial --instruction1 factorial/instruction1.txt --instruction2 factorial/instruction2.txt
    python -m tests.test_factorial
else
    echo "Invalid input"
fi