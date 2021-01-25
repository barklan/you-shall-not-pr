# you-shall-not-pr
You shall not PR.

Rules:
- All code is formatted using _black_
- All .py filenames are in all lowercase characters with no spaces or dashes.
- All functions and variable names follow Python naming conventions!!!
- All function parameters and return values are annotated with Python type hints.
- All imports are sorted alphabetically.
- All files end with a single newline character
- All files do not contain any trailing whitespace

- Avoid global variables.
- Avoid `staticmethod` and limit use of `classmethod`.
- Use google style docstrings

```
repo
├── .github
│   ├── workflows
│   │   ├── ...
│   │   ├── ...
│   │   └── ...
│   └── ...
├── core_package
│   ├── __init__.py
│   ├── ...
├── tests
│   ├── ...
├── conftest.py  # See https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
├── LICENSE
├── README.md
├── .gitignore
├── requirements.txt


```