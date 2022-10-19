#!/bin/zsh

# Simple script to add to ~/.zshrc and ~/.bashrc a django key
# Make sure to have zsh installed!
# The key is passed as first argument or enter from stdin

# If $1 is empty, the script will ask for the key
if [ -r $1 ]
then
    echo -n "Please enter your Django secret key: "
    read KEY
else
    KEY=$1
fi

# Check if the key is valid, by checking if it starts with django-
# Use a for loop to ask for the key again if it is not valid
while [[ $KEY != django-* ]]
do
    echo "The key is not valid, please try again"
    echo -n "Please enter your Django secret key: "
    read KEY
done

function add_key ()
{
    if ! grep -q "DJANGO_KEY" $1; then
        echo "DJANGO_KEY not found in $1, adding it...\n"
        #print export DJANGO_KEY='key' to the end of the file
        echo "export DJANGO_KEY='$KEY'" >> $1
        #echo with green color key added!
        echo -e "\e[32mKey added!\e[0m\n"
    else
        echo "DJANGO_KEY found in $1, make sure to check if it's a functioning key!\n"
        #ask if the user wants to change the key
        echo -n "Do you want to change the key? [y/n]: "
        read CHANGE
        if [ $CHANGE = "y" ]
        then
            #replace the key with the new one
            sed -i.old '/DJANGO/d' $1
            echo "export DJANGO_KEY='$KEY'" >> $1 
            #echo with green color key changed!
            echo -e "\e[32mKey changed!\e[0m\n"
        else
            #print with red color key not changed!
            echo -e "\e[31mKey not changed!\e[0m\n"
        fi
    fi
}

add_key ~/.zshrc
add_key ~/.bashrc

source ~/.zshrc; source ~/.bashrc; exec zsh