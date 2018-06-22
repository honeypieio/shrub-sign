#!/usr/bin/python

from shift import *
import threading
from urllib.request import urlopen
from colorama import Fore

# Check results status
check_pass = Fore.GREEN + "[OK]\t" + Fore.WHITE
check_fail = Fore.RED + "[FAIL]\t" + Fore.WHITE

print("### SIGN SET UP ###\n")

# Check internet connection
try:
	urlopen("https://google.co.uk")
	print(check_pass + "Connected to internet")
except:
	print(check_fail + "Could not establish an internet connection")
	quit()

# Check Murakami
try:
	urlopen("https://murakami.org.uk")
	print(check_pass + "Connected to Murakami")
except:
	print(check_fail + "Could not establish a connection to Murakami")
	quit()

# Retrieve data from Murakami, pass to shift.py
def getNumber():
	# Every ten minutes update display
	threading.Timer(600.0, getNumber).start()
	f = urlopen("https://murakami.org.uk/get-carbon-calculations")
	displayNumber(f.read().decode('utf-8'))

getNumber()
