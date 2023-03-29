"""
This code is Belogs to SME Dehradun Firm. For any query, mail us at schematicslab@gmail.com 
"""

import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer

#BLYNK_AUTH_TOKEN = 'hWRSpWldCWv-ha5aqmasPkbObCIvxNGX'

device1 = 14
device2 = 15
device3 = 23
device4 = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(device1, GPIO.OUT)
GPIO.setup(device2, GPIO.OUT)
GPIO.setup(device3, GPIO.OUT)
GPIO.setup(device4, GPIO.OUT)

# Initialize Blynk
blynk = BlynkLib.Blynk('hWRSpWldCWv-ha5aqmasPkbObCIvxNGX')

# Led control through V0 virtual pin
@blynk.on("V0")
def v0_write_handler(value):
#    global device_switch
    if int(value[0]) is not 0:
        GPIO.output(device1, GPIO.HIGH)
        print('Device1 HIGH')
    else:
        GPIO.output(device1, GPIO.LOW)
        print('Device1 LOW')


# Led control through V1 virtual pin
@blynk.on("V1")
def v1_write_handler(value):
#    global device_switch
    if int(value[0]) is not 0:
        GPIO.output(device2, GPIO.HIGH)
        print('Device2 HIGH')
    else:
        GPIO.output(device2, GPIO.LOW)
        print('Device2 LOW')

# Led control through V2 virtual pin
@blynk.on("V2")
def v2_write_handler(value):
#    global device_switch
    if int(value[0]) is not 0:
        GPIO.output(device2, GPIO.HIGH)
        print('Device3 HIGH')
    else:
        GPIO.output(device2, GPIO.LOW)
        print('Device3 LOW')

# Led control through V3 virtual pin
@blynk.on("V3")
def v3_write_handler(value):
#    global device_switch
    if int(value[0]) is not 0:
        GPIO.output(device3, GPIO.HIGH)
        print('Device4 HIGH')
    else:
        GPIO.output(device1, GPIO.LOW)
        print('Device4 LOW')

#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Alert: Hi! Raspberry Pi Connected to New Blynk2.0") 

while True:
    blynk.run()
