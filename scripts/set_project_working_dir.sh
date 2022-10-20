#!/bin/zsh

# This script adds the working directory of this project to the PYTHON_PROJECT_FOLDER environment variable
cd ..

PYTHON_PROJECT_FOLDER="PYTHON_PROJECT_FOLDER"
PYTHON_PROJECT_PATH=$PWD


function backup_old_path()
{
    # Create a file called .old_paths in the home directory to store old paths
    if [ ! -f $HOME/.old_paths ]
    then
        touch $HOME/.old_paths
    fi
    # Check if the key is already in the file
    if ! grep -q $PYTHON_PROJECT_PATH $HOME/.old_paths
    then
        # If not, add it to the file
        # echo a timestamp and the paths
        echo "[$(date)] $PYTHON_PROJECT_FOLDER = '$PYTHON_PROJECT_PATH'" >> $HOME/.old_paths
    fi
}

function add_proj_dir_path ()
{
    if ! grep -q $PYTHON_PROJECT_FOLDER $1; then
        echo "$PYTHON_PROJECT_FOLDER path not found in $1, adding it...\n"
        echo "export $PYTHON_PROJECT_FOLDER='$PYTHON_PROJECT_PATH'" >> $1
        #echo with green color key added!
        echo -e "\e[32mKey added!\e[0m\n"
    else
        echo "$PYTHON_PROJECT_FOLDER path found in $1, make sure to check if it's a functioning key!\n"
        #ask if the user wants to change the key
        echo -n "Do you want to change the key? [y/n]: "
        read CHANGE
        if [ $CHANGE = "y" ]
        then
            backup_old_path
            sed -i.old '/PYTHON_PROJECT_FOLDER/d' $1
            echo "export $PYTHON_PROJECT_FOLDER='$PYTHON_PROJECT_PATH'" >> $1 
            #echo with green color key changed!
            echo -e "\e[32mKey changed!\e[0m\n"
        else
            #print with yellow color key not changed
            echo -e "\e[33mKey not changed\e[0m\n"
        fi
    fi
}

add_proj_dir_path $HOME/.zshrc
add_proj_dir_path $HOME/.bashrc

cd scripts

source $HOME/.zshrc; source $HOME/.bashrc; exec zsh