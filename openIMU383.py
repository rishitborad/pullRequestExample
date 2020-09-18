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

file_name = './data/OpenIMU385-USB1_'
file_name += random_num
file_name += time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.bin'
fmode = 'wb'

with open(file_name,fmode) as outfile:
    while True:
        try:
            line = ser.readline()
			print("THis is sparta")
            outfile.write(bytes(line))

        except:
            break

    outfile.close()

# all of this ne stuff should go be present in master branch
