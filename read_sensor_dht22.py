#!/usr/bin/python

import sys
import datetime
import adafruit_dht 
import time
import calendar
import board
from time import sleep
sensor = 22
pin = 11

DHT_device = adafruit_dht.DHT22(board.D17)
temperature = DHT_device.temperature
humidity = DHT_device.humidity


if str(sys.argv[1]) == 'temperature':
    while True:
        try:
            temperature = DHT_device.temperature
            humidity = DHT_device.humidity
            # Print what we got to the REPL
            print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
        except RuntimeError as e:
            # Reading doesn't always work! Just print error and we'll try again
            print("Reading from DHT failure: ", e.args)
        sleep(1)