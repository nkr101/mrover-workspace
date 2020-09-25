import smbus
import numpy as np
from math import ceil

# bus initialization
# We initialize bus 2 because that is the only free on on the beaglebone.
bus = smbus.SMBus(2)

# Accelerometer I2C address
I2C_ADDRESS = 0x53

file0 = open("accel0.txt", "w")
file1 = open("accel1.txt", "w")
file2 = open("accel2.txt". "w")

# Relevant registers.
X_LS = 0x32
X_MS = 0x33
Y_LS = 0x34
Y_MS = 0x35
Z_LS = 0x36
Z_MS = 0x37

# I'm just going to use 3 from the spectral code for now,
# FIXME when you know which ones to actually use
muxAddresses = [0x1, 0x2, 0x4]
# FIXME I also just yoinked these from the spectral code
# So I cannot confirm if they are correct
I2C_MUX_ADDRESS = 0x70
MUX_READ_WRITE_REG = 0xCC 

# Reads all data, returns list of X,Y,Z
# random multiplication number is from library apparently,
# IDK was in the starter code, I just moved things around
def read_data():
    global I2C_ADDRESS
    xlsb = bus.read_byte_data(I2C_ADDRESS, X_LS)
    xmsb = bus.read_byte_data(I2C_ADDRESS, X_MS)

    ylsb = bus.read_byte_data(I2C_ADDRESS, Y_LS)
    ymsb = bus.read_byte_data(I2C_ADDRESS, Y_MS)

    zlsb = bus.read_byte_data(I2C_ADDRESS, Z_LS)
    zmsb = bus.read_byte_data(I2C_ADDRESS, Z_MS)

    returnList = []

    x = xmsb << 8
    x = x | xlsb
    x *=  .004 * -9.80665 * 9.80665
    returnList.append(x)

    y = ymsb << 8
    y = y | ylsb
    y *=  .004 * -9.80665 * 9.80665
    returnList.append(y)

    z = zmsb << 8
    z = z | zlsb
    z *=  .004 * -9.80665 * 9.80665
    returnList.append(z)

    return returnList

# Rounds the number to a specified number of decimal places
# TODO can run each data through this if want # decimal places
# RN I'm just giving the data as many points as is
def float_round(num, places = 0, direction = ceil):
    return direction(num * (10**places)) / float(10**places)

def init:
    # Enable ports of the mux
    global muxAddresses
    global I2C_MUX_ADDRESS
    global MUX_READ_WRITE_REG
    for i in range(3):
        bus.write_byte_data(I2C_MUX_ADDRESS, MUX_READ_WRITE_REG, muxAddresses[i])

    # TODO do this three times once for each muxie boy
    bus.write_byte_data(I2C_ADDRESS, 0x2D, 0x08)

def runLoop:
    while True:
        # TODO
        
        # Change mux to 0
        # Read data from 0
        # write data to file 0

        # Repeat for other 2 muxies :)


def main():


    # TODO just basically call functions


    file0.close()
    file1.close()
    file2.close()


if (__name__ == "__main__"):
    main()
