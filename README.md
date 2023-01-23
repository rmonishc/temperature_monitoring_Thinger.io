# temperature_monitoring
I am starting a new project for work. The aim is to build a prototype system that measures temperatures at different locations and sends the data to a server somehow.
So the project will have 2 parts:
- Configuring the RaspberryPi to collect data from a temperature sensor such as DHT22(https://github.com/adafruit/Adafruit_CircuitPython_DHT) and sending the data to
a local server over WiFi. [read_sensor_dht22.py](https://github.com/rmonishc/temperature_monitoring/blob/main/read_sensor_dht22.py) will take care of this.
- Configure the server to receive the incoming data to store it either as a CSV somewhere or inject it into a database. I am thinking of creating a local server running apache with node-js to receive the data from RaspberryPi. Let me know if you have some suggestions or opinions.

Once it is done, I will have to create a dashboard to visualize the data for non-technical users.

# Necessary packages
As you get started with RaspberryPi:
```
$ pip3 install adafruit-circuitpython-dht
$ sudo apt-get install libgpiod2
```

# Code inspirations

https://learn.adafruit.com/dht/dht-circuitpython-code

https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
