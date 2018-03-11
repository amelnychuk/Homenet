import os
import re

from soco import alarms
import datetime
from gtts import gTTS
from House import HouseAI, Zone
from Server import detect_ip_address
import time


import soco



class Event():
    def __init__(self, time):
        pass

    def setTime(self,time):
        self._time = time

    def getTime(self):
        return self._time

    def setZone(self, zone):
        self._zone = zone

    def getZone(self):
        return self._zone

    def add(self):
        pass

    def remove(self):
        pass

    def setStart(self):
        pass

    def setEnd(self):
        pass


class Light(Event):

    #This will build a schedual for the hue lights
    def __init__(self, time):
        super(Light, self).__init__(time)


class Sound(Event, HouseAI):
    """
    Builds an alarm for sonos
    """
    def __init__(self, time):
        super(Sound, self).__init__(time)
        self.startTime = time
        #self.setService(service)
        self.setAlarm()

    def createDataDir(self):
        pass

    def setAlarm(self):

        pass


    def buildMp3(self, msg):
        """

        Args:
            msg: (str) converts text to mp3 and saves it to disk

        Returns:

        """



        filepath = os.path.join(HouseAI.getStorage(), "Notifications")

        filename = "{0}.mp3".format(msg).replace(" ", "")
        pattern = re.compile('[\W_]+')
        pattern.sub('', filename)

        if not os.path.isdir(filepath):
            os.makedirs(filepath)

        outpath = os.path.join(filepath, filename)

        if not os.path.isfile(outpath):
            speech = gTTS(text=msg, lang='en', slow=False)
            speech.save(savefile=outpath)

        self.soundFile = filename

    def __call__(self):
        print "Working"
        self.play_file()

    def play_file(self, port=8000):
        netpath = 'http://{}:{}/{}'.format(detect_ip_address(), port, self.soundFile)
        print("netpath: ", netpath)
        z = HouseAI.getVoice()
        z.volume = 60
        z.play_uri(uri=netpath)




