# coding: utf-8
## @package PCAL6408
#  This is a FaBoGPIO_PCAL6408 library for the FaBo GPIO I2C Brick.
#
#  http://fabo.io/210.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import pkg_resources
SMBUS='smbus'
for dist in pkg_resources.working_set:
    #print(dist.project_name, dist.version)
    if dist.project_name == 'smbus':
        break
    if dist.project_name == 'smbus2':
        SMBUS='smbus2'
        break
if SMBUS == 'smbus':
    import smbus
elif SMBUS == 'smbus2':
    import smbus2 as smbus
import time

## Default I2C Slave Address
SLAVE_ADDRESS = 0x20

# Register Addresses
## Output Register
OUTPUT_REG        = 0x01
## Config Register
CONFIGURATION_REG = 0x03

# OUTPUT Parameter
## IO0_OUTPUT : 0b00000000
IO0_OUTPUT = 0x00
## IO0_INPUT  : 0b00000001
IO0_INPUT  = 0x01
## IO1_OUTPUT : 0b00000000
IO1_OUTPUT = 0x00
## IO1_INPUT  : 0b00000010
IO1_INPUT  = 0x02
## IO2_OUTPUT : 0b00000000
IO2_OUTPUT = 0x00
## IO2_INPUT  : 0b00000100
IO2_INPUT  = 0x04
## IO3_OUTPUT : 0b00000000
IO3_OUTPUT = 0x00
## IO3_INPUT  : 0b00001000
IO3_INPUT  = 0x08
## IO4_OUTPUT : 0b00000000
IO4_OUTPUT = 0x00
## IO4_INPUT  : 0b00010000
IO4_INPUT  = 0x10
## IO5_OUTPUT : 0b00000000
IO5_OUTPUT = 0x00
## IO5_INPUT  : 0b00100000
IO5_INPUT  = 0x20
## IO6_OUTPUT : 0b00000000
IO6_OUTPUT = 0x00
## IO6_INPUT  : 0b01000000
IO6_INPUT  = 0x40
## IO7_OUTPUT : 0b00000000
IO7_OUTPUT = 0x00
## IO7_INPUT  : 0b10000000
IO7_INPUT  = 0x80

## IO0 : 0b00000001
IO0 = 0x01
## IO1 : 0b00000010
IO1 = 0x02
## IO2 : 0b00000100
IO2 = 0x04
## IO3 : 0b00001000
IO3 = 0x08
## IO4 : 0b00010000
IO4 = 0x10
## IO5 : 0b00100000
IO5 = 0x20
## IO6 : 0b01000000
IO6 = 0x40
## IO7 : 0b10000000
IO7 = 0x80

## FaBo GPIO I2C Controll class
class PCAL6408:

    ## Constructor
    #  @param [in] address PCAL6408 I2C slave address default:0x20
    def __init__(self, address=SLAVE_ADDRESS, busnum=1):
        self.bus = smbus.SMBus(busnum)
        self.address = address
        self.output = 0x00
        self.configuration()

    ## Configure Device
    def configuration(self):
        conf = IO0_OUTPUT | IO1_OUTPUT | IO2_OUTPUT | IO3_OUTPUT | IO4_OUTPUT | IO5_OUTPUT | IO6_OUTPUT | IO7_OUTPUT
        self.bus.write_byte_data(self.address, CONFIGURATION_REG, conf)

    ## set Port to Digital
    #  @param [in] port Port
    #  @param [in] output output 1:HIGH, 0:LOW
    def setDigital(self, port, output):
        if output == 1:
            self.output |= port
        elif (output == 0):
            self.output &= ~port
        self.bus.write_byte_data(self.address, OUTPUT_REG, self.output)

    ## All Port to LOW
    def setAllClear(self):
        self.bus.write_byte_data(self.address, OUTPUT_REG, 0x00)
        self.output = 0x00

    ## set Port to GPIO
    #  @param [in] output output
    def setGPIO(self, output):
        self.bus.write_byte_data(self.address, OUTPUT_REG, output)
