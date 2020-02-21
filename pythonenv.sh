#!/bin/bash
sudo apt update
sudo pip install --upgrade pip
virtualenv -p python3 --no-site-package venv
. venv/bin/activate
pip install IPython
pip install openpyxl
pip install numpy
pip install pandas
