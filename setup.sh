#!/bin/bash

#Loads Linux 64 driver for selenium, change if need another system (https://selenium-python.readthedocs.io/installation.html)
driver="https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz"

sudo apt-get install python3.7 python3-venv python3-pip python3-tk

wget $driver

tar -xvzf geckodriver*

chmod a+x geckodriver

sudo mv geckodriver /usr/local/bin

export PATH=$PATH:/usr/local/bin/geckodriver

rm geckodriver*

python3 -m venv env

python3 -m pip install -r requirements.txt

source env/bin/activate

mkdir data

mkdir output

