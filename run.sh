# check if the input string is "factorial" then run the below
if [ "$1" == "factorial" ]; then
    python main.py --repo_path factorial --function_name factorial --instruction1 factorial/instruction1.txt --instruction2 factorial/instruction2.txt
    python -m tests.test_factorial
    python -m py_compile factorial/new_helper.py
    python -m py_compile factorial/new_call.py
elif [ "$1" == "greeting" ]; then
    python main.py --repo_path greeting --function_name greet --instruction1 greeting/instruction1.txt --instruction2 greeting/instruction2.txt
    python -m tests.test_greeting
    python -m py_compile greeting/new_helper.py
    python -m py_compile greeting/new_call.py
else
    echo "Invalid input"
fi