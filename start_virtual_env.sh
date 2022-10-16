#!/bin/zsh

#make sure to have installed virtualenv (pip3 install virtualenv)

#Python version for virtual environment
PYVERSION=3.10

GREEN='\033[0;32m'
BOLD_GREEN='\033[1;32m'
RESET_COLOR='\033[0m'
DEFAULT_COLOR='\033[0m'
RED='\033[0;31m'
YELLOW='\033[0;33m'

#if .venv exists in #PWD, skip, else create it
if [ -d .venv ]; then
    echo "${GREEN}Virtual environment already exists, skipping creation${RESET_COLOR}"
else
    echo "${GREEN}Creating virtual environment..."
    ${PYVERSION} -m venv .venv
    echo "python${PYVERSION} -m venv .venv"
    echo "${BOLD_GREEN}Virtual environment created${RESET_COLOR}"
fi

chmod 755 $PWD/.venv/bin/activate
$PWD/.venv/bin/activate
clear

echo "${BOLD_GREEN}✓ You are now in a python${PYVERSION} virtual environment!\n  ${GREEN}Type exit or ctrl+d to exit${RESET_COLOR}"
exec $SHELL
