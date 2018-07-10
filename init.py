#!/usr/bin/python

from shift import *
import time
import urllib
from colorama import Fore

# Check results status
check_pass = Fore.GREEN + "[OK]\t" + Fore.WHITE
check_fail = Fore.RED + "[FAIL]\t" + Fore.WHITE

checksPassed = False

def checks():

	# Check internet connection
	try:
		urllib.urlopen("https://google.co.uk")
		print(check_pass + "Connected to internet")
	except:
		print(check_fail + "Could not establish an internet connection")
		displayNumber("----")
        	time.sleep(60)
		checksPassed = False
		checks()

	# Check Murakami
	try:
		urllib.urlopen("https://murakami.org.uk")
		print(check_pass + "Connected to Murakami")
		checksPassed = True
	except:
		print(check_fail + "Could not establish a connection to Murakami")
		displayNumber("----")
		checksPassed = False

	if checksPassed == True:
        	 getNumber()
	         time.sleep(600);
		 checks()
        else:
		time.sleep(60)
		checks()

# Retrieve data from Murakami, pass to shift.py
def getNumber():
        f = urllib.urlopen("https://murakami.org.uk/get-carbon-calculations")
        displayNumber(f.read().decode('utf-8'))
checks()
