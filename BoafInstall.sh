#!/bin/bash

echo "install dexter? y/n"
read dexterinstall
if ["$dexterinstall" = "y"]; then
    cd /home/pi/
    mkdir Dexter
    cd Dexter
    git clone https://github.com/DexterInd/GrovePi
    cd /home/pi/Dexter/GrovePi/Script
    bash ./update_grovepi.sh
fi
cd
cd Desktop
cd Boaf
cd Main
cd GPS
gcc -o GPS main.c

cd
cd Desktop/Boaf/Main
cp 98_acm.rules /etc/udev/rules.d/
sudo rm /etc/rc.local
cp rc.local /etc/

echo "Installation complete"