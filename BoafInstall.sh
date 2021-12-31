#!/bin/bash

mkdir ~/Dexter
cd /home/pi/
git clone https://github.com/DexterInd/GrovePi
cd /home/pi/Dexter/GrovePi/Script
bash ./update_grovepi.sh
echo "After installation turn off pi and add grove pi attachment"

cd Main
cd GPS
gcc -o GPS main.c

echo "Installation complete"