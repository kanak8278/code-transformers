# code-transformers

The repository uses poetry for dependency management. To install the dependencies, run the following command:

```bash
poetry install
```
This should install all the dependencies in a virtual environment. To activate the virtual environment, run the following command:

```bash
poetry shell
```

To run the tests and complete generation, run the following command:
```bash
python run.py
```

This will generate the output files in the `examples` directory. Each sub-folder inside the `examples` directory contains a test-set with the following files: `helper.py` and `call.py`.
When we run the `run.py` script, it will generate the following files in each sub-folder: `new_helper.py` as the modified function definition file and `new_call.py` as the modified function call file.

Finally you can see the results on `metrics` in `results.csv` file.