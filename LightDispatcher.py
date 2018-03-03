#imports

import time


from phue import Bridge
from _utils import Color
from Calender import getEventColors


##Testing connecting to the bridge

#register your bridge at phillips website
#get the ip
b = Bridge()
b.connect()

R,G,B = (0.48046875, 0.81640625, 0.28125)


#fade on to orange in deci-seconds


for eventColor in getEventColors():
    print eventColor
    command = {'transitiontime': 30,
               'on': True,
               'bri': 254,
               'xy': Color(eventColor).asCt()}


    b.set_light("Hue color lamp 1", command)
    time.sleep(5)

