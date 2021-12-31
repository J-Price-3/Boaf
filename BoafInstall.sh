#!/bin/bash

cd /home/pi/
mkdir Dexter
cd Dexter
git clone https://github.com/DexterInd/GrovePi
cd /home/pi/Dexter/GrovePi/Script
bash ./update_grovepi.sh
echo "After installation turn off pi and add grove pi attachment"

cd
cd Desktop
cd Boaf
cd Main
cd GPS
gcc -o GPS main.c

echo "Installation complete"