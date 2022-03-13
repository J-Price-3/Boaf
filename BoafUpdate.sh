#!/bin/bash

cd
cd Desktop
rm -r -f Boaf
cd
cd Desktop
git clone https://github.com/Logang2/Boaf.git

cd
cd Desktop
cd Boaf
cd Main
cd GPS
gcc -o GPS main.c

cd
cd Desktop
cd Boaf
cd Main
chmod u+x BoafMain.sh

cd GPS
touch GPSDATA.txt

echo "Update complete"