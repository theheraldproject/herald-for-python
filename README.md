# Herald for Python

Herald for Python provides online Micro Python API and utilities for processing Bluetooth and sensor data from Zephyr devices compiled with the Micropython extensions.
See the Herald for CPP project (TODO link) for that.

This project also holds an interpreter that provides a 'fake' micropython Herald API compatible shim. This is useful for developing Herald Micropython applications on a PC before trying them on a physical device.

## Interpreter

The interpreter acts as a fake Herald wearable, and can inject previously recorded Bluetooth data. You provide your application interface class and the interpreter will execute it, and provide useful error messages when your code has issues.

## Herald API

The Herald folder contains the Python Herald API which is common to Micropython on device and the interpreter. This provides classes that you subclass.