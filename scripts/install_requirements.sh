#!/bin/zsh

# This script generates a requirements.txt file from the current environment
# and installs the packages in the requirements.txt file.
PYVERSION=3.10

pip${PYVERSION} freeze > requirements.txt

# Installing packages from requirements.txt
pip${PYVERSION} install -r requirements.txt