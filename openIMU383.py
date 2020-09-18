import serial
import random

import datetime
import glob
import time

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
            outfile.write(bytes(line))

        except:
            break

    outfile.close()


# all of this ne stuff should go be present in master branch
