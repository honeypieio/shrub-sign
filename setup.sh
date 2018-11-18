#!/bin/bash

sudo cp RPi/motd /etc/motd
sudo cp RPi/rc.local /etc/rc.local

sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install colorama