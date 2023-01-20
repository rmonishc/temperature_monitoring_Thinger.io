# temperature_monitoring
I am starting a new project for work. The aim is to build a prototype system that measures temperatures at different locations and sends the data to a server somehow.
I am thinking of creating a local server running apache with node-js to receive the data from RaspberryPi.
So the project will have 2 parts:
- Configuring the RaspberryPi to collect data from a temperature sensor such as DHT22(https://github.com/adafruit/Adafruit_CircuitPython_DHT) and sending the data to
a local server over WiFi. [https://github.com/rmonishc/temperature_monitoring/blob/main/read_sensor_dht22.py] will take care of this.
- Configure the server to receive the incoming data to store it either as a CSV somewhere or inject it into a database

Once it is done, I will have to create a dashboard to visualize the data for non-technical users.
