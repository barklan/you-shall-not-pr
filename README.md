![Logo](https://.../)

<h2 align="center">You shall not PR.</h2>

<p align="center">

Add here all the badges in the fucking world https://shields.io/

<a href="https://travis-ci.com/psf/black"><img alt="Build Status" src="https://travis-ci.com/psf/black.svg?branch=master"></a>

</p>



### **Guidelines:**
- All functions and variable names follow Python naming conventions!!!
> **That means they should be exactly like plain English except for `_` instead of spaces.**
- Code is formatted using [Black](https://github.com/psf/black)
- All .py filenames are in all lowercase characters with no spaces or dashes.
- All public modules, classes and functions should start with a descriptive docstring.
- All function parameters and return values are annotated with Python [type hints](https://docs.python.org/3/library/typing.html). [For numpy](https://numpy.org/devdocs/reference/typing.html).
- All imports are sorted alphabetically.
- All files end with a single newline character.
- Files do not contain any trailing whitespace.
- Everything should be covered with meaningful tests.

### **Recomendations:**
- Use google style docstrings.
- Avoid global variables.
- Avoid `staticmethod` and limit use of `classmethod`.

### Misc

`conftest.py` is here because of [this](https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada)


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
    - rename everything in setup.py (don't forget to rename numpy)
        - create token in PyPI
        - create a github [secret key](https://docs.github.com/en/actions/reference/encrypted-secrets) `PYPI_API_TOKEN` for that token in github secrets & save locally to .env file
        - remove `repository_url: https://test.pypi.org/legacy/` in workflow if publishing to real index
        - See [tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging) - only tagged commits will be published
    - Setup `MEGA_LOGIN` and `MEGS_PASS` in github secrets
    - ...
    ...

- Create containerized application repo
    1. ...
    2. 
