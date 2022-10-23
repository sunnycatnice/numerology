#!/bin/zsh

# This script adds the working directory of this project to the PYTHON_PROJECT_FOLDER environment variable
cd ..

PYTHON_PROJECT_FOLDER="PYTHON_PROJECT_FOLDER"
PYTHON_PROJECT_PATH=$PWD

#if the first argument is "force", set variable FORCE to true
if [ "$1" = "force" ]; then
    FORCE=true
fi

function backup_old_path()
{
    # Create a file called .old_paths in the home directory to store old paths
    if [ ! -f $HOME/.old_paths ]
    then
        touch $HOME/.old_paths
    fi
    # Check if the path is already in the file
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
        #echo with green color path added!
        echo -e "\e[32mPath added!\e[0m\n"
    else
        echo "$PYTHON_PROJECT_FOLDER path found in $1, make sure to check if it's a functioning path!\n"
        #if force is true, overwrite the path
        if [ "$FORCE" = true ]; then
            backup_old_path
            sed -i.old '/PYTHON_PROJECT_FOLDER/d' $1
            echo "export $PYTHON_PROJECT_FOLDER='$PYTHON_PROJECT_PATH'" >> $1 
            #echo with green color path changed!
            echo -e "\e[32mPath changed!\e[0m\n"
        else
            echo -e "Do you want to overwrite the $PYTHON_PROJECT_FOLDER path in $1? [y/n]"
            read -r answer
            if [ "$answer" = "y" ]; then
                backup_old_path
                sed -i.old '/PYTHON_PROJECT_FOLDER/d' $1
                echo "export $PYTHON_PROJECT_FOLDER='$PYTHON_PROJECT_PATH'" >> $1 
                #echo with green color path changed!
                echo -e "\e[32mPath changed!\e[0m\n"
            else
                #print with yellow color path not changed
                echo -e "\e[33mPath not changed\e[0m\n"
            fi
        fi
    fi
}

add_proj_dir_path $HOME/.zshrc
add_proj_dir_path $HOME/.bashrc

cd scripts

source $HOME/.zshrc; source $HOME/.bashrc;