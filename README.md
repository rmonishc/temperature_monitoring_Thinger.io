# temperature_monitoring
I am starting a new project for work. The aim is to build a prototype system that measures temperatures at different locations and sends the data to a server somehow.
![image](https://user-images.githubusercontent.com/122089762/214335789-120866fd-caeb-47df-a798-37151508be02.png)

After taking a lot of different turns this is what I have:
1. A code on Pi that reads the DHT22 sensor and sends it to a Thinger.io server.
2. There hasn't been much documentation on sending data to Thinger using python. But it was possible to register the device as HTTP device and using requests in Python to send temperature and humidity to the server.

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
