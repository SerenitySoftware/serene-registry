#!/bin/bash

cd /vagrant

echo " "
echo "Beginning Provisioning!"
echo "Please ignore any 'stdin' related errors. It's an Ubuntu+Vagrant bug."
echo " "

echo "Step 1: Updating APT"
apt-get update > /dev/null

echo "Step 2: Installing Required System Packages"
cat dev/requirements.system | xargs apt-get install -y > /dev/null

echo "Step 3: Moving files around"
echo "cd /vagrant" >> /home/vagrant/.bashrc

echo " "
echo " "
echo "Provisioning Complete!"
echo " "
echo "Instructions:"
echo "Type 'vagrant ssh' to connect to your vm."