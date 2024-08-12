local broker:
user: david
password: mckelvie

source bin/activate
https://github.com/eclipse/paho.mqtt.python/tree/master/examples

DHT11 temp sensor
https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup


Issue installing gpio libs in venv, need to install at system level then create venv that pulls in system libs
sudo apt install gpiod
python3 -m venv --system-site-packages ./

Otherwise get errors like 
Traceback (most recent call last):
  File "/home/david/code/led/led.py", line 4, in <module>
    chip = gpiod.Chip('gpiochip4')
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/david/code/led/lib/python3.11/site-packages/gpiod/chip.py", line 58, in __init__
    self._chip = _ext.Chip(path)
                 ^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory
