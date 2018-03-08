import os


from soco import alarms
import datetime.time as time
from gtts import gTTS
from House import House




class Event(object):
    def __init__(self, time, zone):
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


    def buildMp3(self, msg):
        """

        Args:
            msg: (str) converts text to mp3 and saves it to disk

        Returns:

        """



        filepath = os.path.join(House.getStorage(), "Notifications")
        filename = "{0}.mp3".format(msg)

        if not os.path.isdir(filepath):
            os.makedirs(filepath)

        outpath = os.path.join(filepath, filename)

        if not os.path.isfile(outpath):
            speech = gTTS(text=msg, lang='en', slow=False)
            speech.save(savefile=outpath)

        self.soundFile = outpath

    def __call__(self):
        pass

