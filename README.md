# temperature_monitoring
I am starting a new project for work. The aim is to build a prototype system that measures temperatures at different locations and sends the data to a server somehow.
![image](https://user-images.githubusercontent.com/122089762/214335789-120866fd-caeb-47df-a798-37151508be02.png)

So the project will have 2 parts:
- Configuring the RaspberryPi to collect data from a temperature sensor such as DHT22(https://github.com/adafruit/Adafruit_CircuitPython_DHT) and sending the data to
a local server over WiFi. [read_sensor_dht22.py](https://github.com/rmonishc/temperature_monitoring/blob/main/read_sensor_dht22.py) will take care of this.
- Configure the server to receive the incoming data to store it either as a CSV somewhere or inject it into a database. I am thinking of creating a local server running apache with node-js to receive the data from RaspberryPi. Let me know if you have some suggestions or opinions.

(This layout has been modified owing to the complications of creating a local server in the premises. Another solution being tried is to save the values in the Pi itself and periodically access and move the values from another PC that will serve as the 'server'. Any opinion on this idea is welcomed)

Once it is done, I will have to create a dashboard to visualize the data for non-technical users.

# Necessary packages
As you get started with RaspberryPi:
```
$ pip3 install adafruit-circuitpython-dht
$ sudo apt-get install libgpiod2
```



Dash could be used to further enhance visualizations if needed

# Code inspirations

https://learn.adafruit.com/dht/dht-circuitpython-code

https://medium.com/initial-state/how-to-build-a-raspberry-pi-temperature-monitor-8c2f70acaea9
