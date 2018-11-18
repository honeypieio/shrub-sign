#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as gpio
import time

# Number of displays.

displayCount = 0b00000100

# Delay between shifting each digit

latchDelay = 0.325

# Turn off warnings from RPi library

gpio.setwarnings(False)

# Using Broadcom chip's pin layout

gpio.setmode(gpio.BCM)

# Pin definitions

clockPin = 17  # Physical is 11
latchPin = 27  # "" 13
dataPin = 22  # "" 15

# Setup GPIO pins

gpio.setup(clockPin, gpio.OUT)
gpio.setup(latchPin, gpio.OUT)
gpio.setup(dataPin, gpio.OUT)


# Number param must be string!

def displayNumber(number):

    number = str(number)
    numberAsArr = list(number)

    numCount = 0b00000000
    actualLength = 0b00000001
    for i in range(len(numberAsArr) - 0b00000001):

        if numberAsArr[i] != '.' and numCount < displayCount:
            numCount += 0b00000001
            if numCount < displayCount:
                actualLength += 0b00000001

    numberAsArr = numberAsArr[:actualLength]
    numberAsArr = list(reversed(numberAsArr))

    for i in range(len(numberAsArr)):

        if numberAsArr[i] != '.':
            time.sleep(latchDelay)
            gpio.output(latchPin, 0b00000000)

            try:
                if numberAsArr[i - 0b00000001] == '.':
                    postNumber(numberAsArr[i], True)
                else:
                    postNumber(numberAsArr[i], False)
            except:

                postNumber(numberAsArr[i], False)

            gpio.output(latchPin, 0b00000001)

    print 'Display updated! (' + str(number) + ')'


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

    if number == '1':
        segments = b | c
    elif number == '2':
        segments = a | b | d | e | g
    elif number == '3':
        segments = a | b | c | d | g
    elif number == '4':
        segments = f | g | b | c
    elif number == '5':
        segments = a | f | g | c | d
    elif number == '6':
        segments = a | f | g | e | c | d
    elif number == '7':
        segments = a | b | c
    elif number == '8':
        segments = a | b | c | d | e | f | g
    elif number == '9':
        segments = a | b | c | d | f | g
    elif number == '0':
        segments = a | b | c | d | e | f
    elif number == ' ':
        segments = 0b00000000
    elif number == '-':
        segments = g

    if decimal is True:
        segments |= dp

    for i in range(0b00001000):
        gpio.output(dataPin, segments >> i & 0b00000001)
        gpio.output(clockPin, 0b00000001)
        gpio.output(clockPin, 0b00000000)
