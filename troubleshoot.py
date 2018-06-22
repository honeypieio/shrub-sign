#!/usr/bin/python3

from urllib.request import urlopen

from colorama import Fore

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


try:
	urlopen("https://murakami.org.uk")
	print(check_pass + "Connected to Murakami")
except:
	print(check_fail + "Could not establish a connection to Murakami")
	quit()
