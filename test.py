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
def displayNumber():

    gpio.output(latchPin, 0)

    postNumber(0b01000000)

    gpio.output(latchPin, 1)

# Find byte according to number, shift to registers
def postNumber(byte):

    a = 0b10000000
    b = 0b00000010
    c = 0b00000100
    d = 0b00001000
    e = 0b00010000
    f = 0b01000000
    g = 0b00100000
    dp = 0b00000001

    for i in range(8):
        gpio.output(dataPin, (byte >> i) & 1)
        gpio.output(clockPin, 1)
        gpio.output(clockPin, 0)

displayNumber()
