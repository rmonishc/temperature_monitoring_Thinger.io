#!/usr/bin/python

import sys
import datetime
import adafruit_dht
import board
from time import sleep
from collections import deque

#initializing device and reading data
DHT_device = adafruit_dht.DHT22(board.D17)
temperature = DHT_device.temperature
humidity = DHT_device.humidity

#setting frequency to read data
number_of_seconds_to_sleep = 5

#initiating temperature as deque

while True:
    try:
        temperature = DHT_device.temperature
        humidity = DHT_device.humidity
        time_now = datetime.datetime.now().strftime('%H:%M:%S')
        # Print what we got to the REPL
        print("{} Temp: {:.1f} *C \t Humidity: {}%".format(time_now, temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)
    sleep(number_of_seconds_to_sleep)