
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
ser.flushInput()

random_num = str(random.randint(100,10000))

name = './OpenIMU_'
name += random_num
name += time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.bin'
mode = 'wb'

with open(name,fmode) as outf:
    while True:
        try:
            line = ser.readline()
            print(bytes(line))
            outf.write(bytes(line))

        except:
            break

    outf.close()

#time.sleep(60)
#print('Pushing to Azure ...')
#toCloud = push2azure()
#toCloud.push2AzureAsBlobs()
