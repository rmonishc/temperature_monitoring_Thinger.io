#!/usr/bin/python

import datetime
import adafruit_dht
import board
from time import sleep
import requests
import csv
import os

#initializing device and reading data
DHT_device = adafruit_dht.DHT22(board.D17)
temperature = DHT_device.temperature
humidity = DHT_device.humidity

#setting frequency to read data
number_of_seconds_to_sleep = 60

#function to check if the desired CSV file exists
def check_dir(file_name):
    directory = os.path.dirname(file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)

while True:
    try:
        #read the sensor
        temperature = DHT_device.temperature
        humidity = DHT_device.humidity

        #using the date as the csv file name, that way every day a file will be created
        csv_filenow = str(datetime.date.today())
        time_now = datetime.datetime.now().strftime('%H:%M:%S')
        
        check_dir('./CSV_FILES/' + csv_filenow + '.csv')

        #Appending to CSV
        with open('./CSV_FILES/' + csv_filenow + '.csv', 'a') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            #writing data into the csv file
            writer.writerow([time_now, temperature, humidity])
        sleep(number_of_seconds_to_sleep)
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)


