#!/bin/sh
# Chandra Veeramreddy 2019
echo 'Installing ActiveMQ Prereqs...'
sudo yum install update -y
sudo yum install java-1.8.0-openjdk -y
#sudo curl "https://bootstrap.pypa.io/get-pip.py" | python3
#sudo pip3 install -r requirements.txt
echo '---------------------------------------------------'
echo 'Install complete! run: python ActiveMQ.py to start'