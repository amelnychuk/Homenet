from phue import Bridge
import numpy as np
from _utils import Color

##Testing connecting to the bridge

#register your bridge at phillips website
#get the ip
b = Bridge()
b.connect()



#fade on to orange
command =  {'transitiontime' : 10,
            'on' : True,
            'bri' : 254,
            'xy' : Color(1,.7,0).asCt()}


b.set_light("Hue color lamp 1", command)


