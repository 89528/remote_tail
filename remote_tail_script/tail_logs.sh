#!/bin/bash

echo "Enter ip"
read ip
echo "Enter log path"
read path
while true; do
    ssh noc@$ip tail -f $path
   # trap break INT
    read -p "Do you wish to install this program?" yn
    case $yn in
        [Yy]* ) tail -f $path;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
