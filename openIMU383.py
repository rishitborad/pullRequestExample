
"""
Program to log OpenIMU335 data
Created on 2020-02-14
@author: xiankw
"""

import serial
import time
import datetime
import glob
import random

ser = serial.Serial('/dev/cu.usbserial-FT8YAYV7', 921600, parity='N',bytesize=8,stopbits=1,timeout=None) # need to confirm port


while True:
    if ser.isOpen(): break

print ('\Port is open now\n')
#configFRII(ser)
ser.flushInput()

random_num = str(random.randint(100,10000))

fname = './data/OpenIMU385-USB1_'
fname += random_num
fname += time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.bin'
fmode = 'wb'

with open(fname,fmode) as outf:
    while True:
        try:
            line = ser.readline()
            print(bytes(line))
            outf.write(bytes(line))

        except:
            break

    outf.close()
