# You shall not PR.

`pip install pre-commit` and `pre-commit install` from local env to set up hooks

### **Rules (will not pass automated tests otherwise):**
- All functions and variable names follow Python naming conventions!!!
> **That means they should be exactly like plain English except for `_` instead of spaces.
- Code is formatted using _black_
- All .py filenames are in all lowercase characters with no spaces or dashes.
- Files should start with a docstring describing the contents and usage of the module.
- All public functions and classes should start with a docstring.
- All function parameters and return values are annotated with Python type hints. [For numpy](https://numpy.org/devdocs/reference/typing.html)
- All imports are sorted alphabetically.
- All files end with a single newline character
- All files do not contain any trailing whitespace

### **Recomendations:**
- Use google style docstrings
- Avoid global variables.
- Avoid `staticmethod` and limit use of `classmethod`.

### Misc

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

[PyPA](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

Packaging:
https://packaging.python.org/tutorials/packaging-projects/

https://github.com/marketplace/actions/pypi-publish