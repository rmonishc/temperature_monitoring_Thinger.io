# temperature_monitoring
I am starting a new project for work. The aim is to build a prototype system that measures temperatures at different locations and sends the data to a server somehow.
![image](https://user-images.githubusercontent.com/122089762/214335789-120866fd-caeb-47df-a798-37151508be02.png)

After taking a lot of different turns this is what I have:
1. A code on Pi, [pushing_thinger.py](https://github.com/rmonishc/temperature_monitoring/blob/main/pushing_thinger.py), that reads the DHT22 sensor and sends it to a Thinger.io server. Setup a crontab to start the python program on reboot.
2. There hasn't been much documentation on sending data to Thinger using python. But it was possible to register the device as HTTP device and using requests in Python to send temperature and humidity to the server. All you need is the Bearer authenitication token and the url that Thinger.io provides you. Create a bucket to put in the values, and a dashboard to visualize and you have it.

And Voilà

![image](https://user-images.githubusercontent.com/122089762/217532894-14f27364-351b-4c36-ab30-eef6cf0b0d59.png)


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
