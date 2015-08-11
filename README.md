## Purpose


### Background

783 million people in the world do not have access to safe water. This is roughly 11 percent of the world's population.
2.5 billion people in the world do not have access to adequate sanitation, this is about 35 percent of the world's population.
Around 700,000 children die every year from diarrhea caused by unsafe water and poor sanitation – that's almost 2,000 children a day.

System Name | Initial Cost (US dollars) | Liters of Water per Dollar (long term)
----- | --- | ---
a) Flame-heated water pot (heated to boiling with no pasteurization indicator) | small | 50
b) Flame-heated water pot with pasteurization indicator | 3 | 96
c) Solar Box Cooker with pasteurization indicator | 23 | 375

### Data

Contrary to what many people believe, it is not necessary to boil water to make it safe to drink. Also contrary to what many people believe, it is usually not necessary to distill water to make it safe to drink. Heating water to 65º C (149º F) will kill all germs, viruses, and parasites.3 This process is called pasteurization and its use for milk is well known. [source][1]

### Design
Based on [Heaven's Flame][2]

### Primary Goals:
* Heat 1 quart water to 149 degrees fahrenheit for 5 minutes.
* Come up with a simple design that could be cheaply reproducible.
* 

### Notifications
Twitter monitor account [@Solar_purifier][4]


### Build it

    virtualenv venv
    pip install -r requirements.txt

### Libraries

[Thermometer] [3]


[1]: http://solarcooking.org/pasteurization/solarwat.htm "A SUMMARY OF WATER PASTEURIZATION TECHNIQUES"
[2]: http://www.backwoodshome.com/articles/radabaugh30.html "Heaven's Flame"
[3]: http://www.raspberrypi-spy.co.uk/2013/03/raspberry-pi-1-wire-digital-thermometer-sensor/ "Raspberry Pi 1- Wire Digital Thermometer Sensor (DS18B20)"
[4]: http://twitter.com/solar_purifier