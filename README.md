# Introduction 

This is a starter template for Prism team python packages.

# Getting Started

Easy way to use
1.	Create new empty project repo
2.	Clone your new repo down
3.	Clone this repo
4.	Copy the files from this repo into your new repo

# Customize Setup

1.  Goto setup.py
2.  Update 'name' to your package name (kebab case)
3.  Update 'description' to a simple short description.
4.  Update author and author_email to yourself
5.  Set 'url' to Azure Devops clone url for your project
6.  Ensure classifiers covers your python version, OS restrictions if necessary
7.  Set 'python_requires' to minimum version needed, recommended to use '>=3.7'
8.  Set 'install_requires' to be the exact packages needed for
packages to be used (should be similar to requirements.txt minus testing and non-package required tools)
9.  Update the folder 'greeting_service' to be the 'name' of your package (usually repo name) 


# Build and Test

- run 'python -m venv ./venv'
- run 'python -m pip install --upgrade pip'
- run 'python -m pip install --upgrade setuptools wheel keyring artifacts-keyring'
- run 'cp pip.ini ./venv'
- run 'pip install -r ./requirements.txt'
- run 'pytest' to run tests

You should be good to go!

# File descriptions

- .coveragerc => custom settings for python coverage tests
- .gitignore => files you want to ignore for commit history
- config.json => base configuration variables, should be used in testing but consider replacing most settings with env variables in non-local apps
- pytest.ini => defines custom settings for pytest, this file includes declaration for 'should' based behavior styled unit tests
- requirements.txt => packages required for development of this package
- setup.py => instructions for creating tar and wheel files for package sharing (used to package wheel for Azure Devops Artifacts)

# Versioning

- Follows [semver](https://semver.org/)
- Update 'version' in setup.py when adding new features or else builds will fail

# Notes

- src/tests follows structure provided by pytest good practices docs here:
    - https://docs.pytest.org/en/latest/goodpractices.html
    - https://blog.ionelmc.ro/2014/05/25/python-packaging/