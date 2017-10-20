# coding: utf-8
## @package FaBoGPIO_PCAL6408.py
#  This is a library for the FaBo GPIO I2C Brick.
#
#  http://fabo.io/210.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoGPIO_PCAL6408
import time
import sys

pcal6408 = FaBoGPIO_PCAL6408.PCAL6408()

try:
    while True:
        for i in range(8):
            pcal6408.setDigital(1<<i, 1)
            time.sleep(1)

        pcal6408.setAllClear()
        time.sleep(1)

except KeyboardInterrupt:
    pcal6408.setAllClear()
    sys.exit()
