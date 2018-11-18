# Carbon Sign
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
Firmware for driving 7 segment displays via shift registers.
*Instructions on how to login including the password are available on the Passbolt server.*

## Installation
1. `git clone https://github.com/honeypieio/shrub-sign` 
2. Update `RPi/rc.local` with repo directory (assumes `/home/pi/shrub-sign`)
3. `./setup.sh`

The sign will start displaying upon rebooting.

## Troubleshooting

### The sign displays four dashes ("----")
This means the sign was unable to fetch the carbon savings over the internet.

* **Does the WiFi work?**
    Use a device you know works to access the internet (visit google.co.uk, for example)
* **Is Murakami online?** (visit murakami.org.uk)
    Use a device you know works and visit murakami.org.uk on your browser. 

If yes to both questions above, the sign isn't connected to the WiFi. Please login and update the WiFi settings as per the instructions in `RPi/motd`.

### Nothing is displayed

* **Try unplugging the sign, waiting 30 seconds, then plugging it back in.**
    If the sign lights up randomly, wait a minute - this should resolve itself.
    If the sign does not light at all at any point after a minute, please continue to the next step.

* **Check if there is a green flashing LED (light) on the Raspberry Pi. (green board on the back of the sign)**
    If the LED is not flashing, the Raspberry Pi or the voltage regulator is dead </\3
    If the LED is flashing, the firmware has encountered an error. Login and follow instructions (errors will be printed to the screen)

### The wrong number is displayed!
Turn the sign off and on again.