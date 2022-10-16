#!/bin/zsh

#make sure to have installe virtualenv (pip3 install virtualenv)
python3.10 -m venv .

echo "Rebooting shell to activate virtual environment..."
echo "Done!"
echo "To exit virtual environment type: exit"
exec $SHELL
