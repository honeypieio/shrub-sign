#!/usr/bin/python

import RPi.GPIO as gpio

# Using Broadcom chip's pin layout
gpio.setmode(gpio.BCM)

# Pin definitions
clockPin = 17 # Physical is 11
latchPin = 27 # "" 13
dataPin = 22 # "" 15

# Setup GPIO pins
gpio.setup(clockPin, gpio.OUT)
gpio.setup(latchPin, gpio.OUT)
gpio.setup(dataPin, gpio.OUT)


# Number param must be string!
def displayNumber(number):

    number = str(number)
    numberAsArr = list(number);
    formattedNumber = []
    count = 0
    for i in range(len(numberAsArr)):
	if numberAsArr[i] != "" and i < (len(numberAsArr) - 1):

	    gpio.output(latchPin, 0)

	    count = count + 1
            if numberAsArr[i+1] == ".":
	        numberAsArr[i+1] = ""
        	postNumber(int(numberAsArr[i]), True)
	    else:
		postNumber(int(numberAsArr[i]), False)

            gpio.output(latchPin, 1)

# Find byte according to int, shift to registers

def postNumber(number, decimal):

    a = 1<<0
    b = 1<<6
    c = 1<<5
    d = 1<<4
    e = 1<<3
    f = 1<<1
    g = 1<<2
    dp = 1<<7

    number = int(number)

    if number == 1:
        segments = b | c
    elif number == 2:
         segments = a | b | d | e | g
    elif number == 3:
         segments = a | b | c | d | g
    elif number == 4:
        segments = f | g | b | c
    elif number == 5:
        segments = a | f | g | c | d
    elif number == 6:
        segments = a | f | g | e | c | d
    elif number == 7:
        segments = a | b | c
    elif number == 8:
        segments = a | b | c | d | e | f | g
    elif number == 9:
        segments = a | b | c | d | f | g
    elif number == 0:
        segments = a | b | c | d | e | f


    if decimal == True:
        segments |= dp;

    for i in range(8):
        gpio.output(dataPin, (segments >> i) & 1)
	gpio.output(clockPin, 1)
        gpio.output(clockPin, 0)
