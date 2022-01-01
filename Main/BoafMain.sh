#!/bin/bash

source ./BoafMain.sh

sudo ./GPS/GPS &

python BoafPosition.py &