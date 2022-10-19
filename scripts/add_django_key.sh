#!/bin/zsh

#simple script to add to ~/.zshrc and ~/.bashrc a django key
#make sure to have zsh installed!
#the key is passed as first argument or enter from stdin

#if $1 is empty, the script will ask for the key
if [ -r $1 ]
then
    echo -n "Please enter your Django secret key: "
    read KEY
else
    KEY=$1
fi

#check if the key is valid, by checking if it starts with django-
#use a for loop to ask for the key again if it is not valid
while [[ $KEY != django-* ]]
do
    echo "The key is not valid, please try again"
    echo -n "Please enter your Django secret key: "
    read KEY
done

if ! grep -q "DJANGO_KEY" ~/.zshrc; then
    echo "DJANGO_KEY not found in ~/.zshrc, adding it...\n"
    #print export DJANGO_KEY='key' to the end of the file
    echo "export DJANGO_KEY='$KEY'" >> ~/.zshrc
    #echo with green color key added!
    echo -e "\e[32mKey added!\e[0m\n"
else
    echo "DJANGO_KEY found in ~/.zshrc, make sure to check if it's a functioning key!\n"
    #ask if the user wants to change the key
    echo -n "Do you want to change the key? [y/n]: "
    read CHANGE
    if [ $CHANGE = "y" ]
    then
        #replace the key with the new one
        sed -i.old '/DJANGO/d' ~/.zshrc
        echo "export DJANGO_KEY='$KEY'" >> ~/.zshrc 
        #echo with green color key changed!
        echo -e "\e[32mKey changed!\e[0m\n"
    else
        echo "Key not changed!\n"
    fi
fi

if ! grep -q "DJANGO_KEY" ~/.bashrc; then
    echo "DJANGO_KEY not found in ~/.bashrc, adding it...\n"
    printf "\nexport DJANGO_KEY='$KEY'" >> ~/.bashrc;
    #echo with green color key added!
    echo -e "\e[32mKey added!\e[0m\n"
else
    echo "DJANGO_KEY found in ~/.bashrc, make sure to check if it's a functioning key!\n"
fi

source ~/.zshrc; source ~/.bashrc; exec zsh