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

gpio.output(clockPin, gpio.LOW)
gpio.output(latchPin, gpio.LOW)
gpio.output(dataPin, gpio.LOW)


# Number param must be string!
def showNumber(number):

    numberAsArr = list(number);

    for i in range(4):

        if numberAsArr[i] == ".":
            del numberAsArr[i];
	
        if numberList[i+1] == "." and (i+1) != 4:
            postNumber(numberAsArr[i], true)
                
        else:
            postNumber(numberAsArr[i], false)

        gpio.output(latchPin, gpio.LOW)
        gpio.output(latchPin, gpio.HIGH)

def postNumber(number, decimal):

    a = 1<<0
    b = 1<<6
    c = 1<<5
    d = 1<<4
    e = 1<<3
    f = 1<<1
    g = 1<<2
    dp = 1<<7


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
    else:
        segments = g


    if decimal == true: 
        segments |= dp;

    for i in range(8):
        gpio.output(clockPin, gpio.LOW)
        gpio.output(dataPin, segments & 1 << (7 - i))
        gpio.output(clockPin, gpio.HIGH)
        print(segments & 1 << (7 - i));
