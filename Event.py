

from soco import alarms
import datetime.time as time
from gtts import gTTS
from House import House

class event():

    def __init__(self):
        #color of lights
        self._color = [1,1,1]
        self._Instruction = ""
        self._devices = []

    #ramp up time
    #ramp down time

    #device data


class Event(object):
    def __init__(self, time, zone):
        pass

    def setTime(self,time):
        self._time = time

    def getTime(self):
        return self._time

    def setZone(self,zone):
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
    def __init__(self, time, zone):
        super(Light, self).__init__(time, zone)


class Sound(Event, House):
    """
    Builds an alarm for sonos
    """
    def __init__(self, time, zone, service):
        super(Sound, self).__init__(time, zone)
        self.startTime = time
        #self.setService(service)
        self.setAlarm()

    def createDataDir(self):
        pass

    def setAlarm(self):

        pass


    def buildMp3s(self, msg):
        speech = gTTS(text=msg, lang='en', slow=False)
        speech.save(savefile="House.Data/msg,mp3")
