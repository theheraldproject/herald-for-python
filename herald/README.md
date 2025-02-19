# Herald API for Python

This Python module provides the high level API that allows your analysis applications to receive data on nearby Bluetooth devices and sensor data. It also provides
a link to the built in Herald Analysis API giving you in-memory real time analysis and aggregated summaries of sensor data over time, from minutes to months!

## Creating your own application

To create a HeraldApplet for execution on a device or in the interpreter, create yourself a new Python file. 

Within this file create a new class that subclasses the HeraldApplet class in the micropython.py file in this API.

## Testing your application in the interpreter

TODO the interpreter hasn't been created yet, but it will allow you to do things like the below:-

```sh
python ./interpreter/main.py -a path/to/my/app/app.py
```

Note by default that the interpreter will generate fake RSSI proximity data for simulated nearby devices in the same manner as expected for human interaction and detection by a real device.

TODO also allow replay of a previously recorded set of data (E.g. operation outbreak data).