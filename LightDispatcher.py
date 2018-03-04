#imports

import time


from phue import Bridge
from _utils import Color
from gtts import gTTS
from Calender import getEventColors
import Speaker


##Testing connecting to the bridge

#register your bridge at phillips website
#get the ip
b = Bridge()
b.connect()

R,G,B = (0.48046875, 0.81640625, 0.28125)


#fade on to orange in deci-seconds
zone = Speaker.getZone()
server = Speaker.HttpServer(8000)
server.start()
for eventTxt, eventColor in getEventColors():
    print eventColor
    command = {'transitiontime': 30,
               'on': True,
               'bri': 254,
               'xy': Color(eventColor).asCt()}

    speech = gTTS(text=eventTxt, lang='en', slow=False)
    mp3file = (eventTxt + ".mp3").replace(" ","")

    speech.save(mp3file)
    print ("Print saved file: {}".format(mp3file))
    Speaker.play_file(zone, mp3file, port=8000)


    b.set_light("Hue color lamp 1", command)
    time.sleep(5)


b.set_light("Hue color lamp 1", 'on', False)



time.sleep(5)
server.stop()