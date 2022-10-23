#!/bin/zsh

# Make sure to have installed virtualenv (pip3 install virtualenv)

# Python version for virtual environment
PYVERSION=3.10

GREEN='\033[0;32m'
BOLD_GREEN='\033[1;32m'
RESET_COLOR='\033[0m'
DEFAULT_COLOR='\033[0m'
RED='\033[0;31m'
YELLOW='\033[0;33m'

#do not ask yes/no questions and update the path of the project
/bin/zsh ./set_project_working_dir.sh force

# Create a virtual environment
if [ -d .venv ]; then
    echo "${GREEN}Virtual environment already exists, skipping creation${RESET_COLOR}"
else
    echo -n "${GREEN}Creating virtual environment with "
    echo "python${PYVERSION} -m venv .venv"
    python${PYVERSION} -m venv $PYTHON_PROJECT_FOLDER/.venv
    echo "${BOLD_GREEN}Virtual environment created${RESET_COLOR}"
fi

# chmod 755 $PYTHON_PROJECT_FOLDER/.venv/bin/activate
# $PYTHON_PROJECT_FOLDER/.venv/bin/activate

echo "${BOLD_GREEN}✓ You are now in a python${PYVERSION} virtual environment!" 
echo "  ${GREEN}Type ${BOLD_GREEN}exit${GREEN} or ${BOLD_GREEN}ctrl+d${GREEN} ${RED}to exit${RESET_COLOR}"
echo "  ${GREEN}If you find yourself in VScode you may be by default in a python virtual env.${RESET_COLOR}"
echo "  ${GREEN}If you want to exit the virtual env, type ${YELLOW}deactivate${GREEN} in the terminal${RESET_COLOR}"
exec $SHELL
