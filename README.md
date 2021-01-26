![Logo](https://.../)

<h2 align="center">You shall not PR.</h2>

<p align="center">

Add here all the badges in the fucking world https://shields.io/

<a href="https://travis-ci.com/psf/black"><img alt="Build Status" src="https://travis-ci.com/psf/black.svg?branch=master"></a>

</p>

### Setup

1. Create environment and install requirements_dev.txt:

```bash
conda create -n foo python=3.9
conda activate foo
```
or

```bash
python -m venv env
source env/bin/activate
# or env/Scripts/activate.bat if on Windows
```

2. Install pre-commit

```bash
python -m pip install pre-commit
cd foo
pre-commit install
```

### **Rules (will not pass automated tests otherwise):**
- All functions and variable names follow Python naming conventions!!!
> **That means they should be exactly like plain English except for `_` instead of spaces.**
- Code is formatted using _black_
- All .py filenames are in all lowercase characters with no spaces or dashes.
- Files should start with a docstring describing the contents and usage of the module.
- All public functions and classes should start with a docstring.
- All function parameters and return values are annotated with Python type hints. [For numpy.](https://numpy.org/devdocs/reference/typing.html)
- All imports are sorted alphabetically.
- All files end with a single newline character.
- Files do not contain any trailing whitespace.

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
├── conftest.py
├── LICENSE
├── README.md
├── .gitignore
├── requirements.txt

```

`conftest.py` is here because of [this](https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada)

[PyPA](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

Packaging:
https://packaging.python.org/tutorials/packaging-projects/

https://github.com/marketplace/actions/pypi-publish

### Sf

- Any color you like, just so it does not conflict with PyPI
- Create core python package repo
    - copy this repo, rename core_package, rename first line in `.pre-commit-config.yaml`
    - Setup test workflow
    - Setup codecov [link](https://docs.codecov.io/docs/quick-start)
        - register repo on codecov
        - install github codecov app for repo
        - modify workflows file, specifically CODECOV_TOKEN
        - first run tests locally to make an initial assessment
    - rename everything in setup.py
        - create token in PyPI
        - create a github [secret key](https://docs.github.com/en/actions/reference/encrypted-secrets) `PYPI_API_TOKEN` for that token in github settings & save locally to .env file
        - remove `repository_url: https://test.pypi.org/legacy/` in workflow if publishing to real index
        - See [tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging) - only tagged commits will be published
    
    - Setup mkdocs --> readthedocs
    - ...
    ...

- Create containerized application repo
    1. ...
