#!/usr/bin/python

import RPi.GPIO as gpio
import time

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
    numberAsArr = list(number)

    numCount = 0
    actualLength = 1
    for i in range(len(numberAsArr) - 1):

	if numberAsArr[i] != "." and numCount < 4:
	    numCount+=1
        if numCount < 4:
	    actualLength+=1

    numberAsArr = numberAsArr[:actualLength]
    numberAsArr = list(reversed(numberAsArr))

    for i in range(len(numberAsArr)):

        if numberAsArr[i] != ".":
	    time.sleep(0.325);
            gpio.output(latchPin, 0)

            try:
                if numberAsArr[i-1] == ".":
                    postNumber(int(numberAsArr[i]), True)
                else:
                    postNumber(int(numberAsArr[i]), False)

            except:
                postNumber(int(numberAsArr[i]), False)

            gpio.output(latchPin, 1)

    print("Display updated! (" + str(number) + ")")

# Find byte according to number, shift to registers
def postNumber(number, decimal):

    a = 0b10000000
    b = 0b00000010
    c = 0b00000100
    d = 0b00001000
    e = 0b00010000
    f = 0b01000000
    g = 0b00100000
    dp = 0b00000001


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
        segments |= dp

    #print(format(segments, "08b"))

    for i in range(8):
        gpio.output(dataPin, (segments >> i) & 1)
        gpio.output(clockPin, 1)
        gpio.output(clockPin, 0)
