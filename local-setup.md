# Local development

## Pre-requisites

I'm using [`pyenv`](https://github.com/pyenv/pyenv-virtualenv) to easily manage python versions. Some of the following commands use `pyenv`.
Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for easy installation. Then add pyenv-virtualenv plugin to it.

### Configure local development setup

 - Install and activate python 3.8.1 in the root directory
    - `pyenv install 3.8.1`
    - `pyenv virtualenv 3.8.1 uniquenames`
    - `pyenv local uniquenames`

 - Install precommit hook
    - `pre-commit install`

You're all set to hack!

Before making changes, let's ensure tests run successfully on local.

### Running Tests

 - Run all tests with coverage
    - `coverage run -m pytest -v`
 - Show report in terminal
    - `coverage report -m`


### Checklist before publishing the package

 - Install `pip install twine --dev`
 - Bump the version constant `VERSION` in `setup.py`
 - Run setup test
    - `python setup.py test`
 - Publish package to PyPI
    - `python setup.py upload`
 - Enter PyPi credentials (note: you must be added to the project as a maintainer)
