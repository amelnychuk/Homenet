"""
Brain controls all sensors
"""

import os

import soco
import schedule

from Server import HttpServer, detect_ip_address



class CaseInsensitiveDict(dict):

    def __init__(self, *args, **kwargs):
        super(CaseInsensitiveDict, self).__init__(*args, **kwargs)
        self._convert_keys()

    def __setitem__(self, key, value):
        super(CaseInsensitiveDict, self).__setitem__(key.lower().replace(" ",""), value)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower().replace(" ",""))

    def _convert_keys(self):
        for k in list(self.keys()):
            v = super(CaseInsensitiveDict, self).pop(k)
            self.__setitem__(k, v)

def setStorage():
    path = os.path.join(os.getcwd(), "mp3")
    if os.path.isdir(path):
        return path
    else:
        os.makedirs(path)
        return path

class Brain(object):
    """
    Collects up all the devices in the home.
    Data and HTTP link

    """

    scheduler = schedule.Scheduler()
    storage = setStorage()
    voice = list(soco.discover())[0].group.coordinator

    def __init__(self):
        print "Discovering devices..."
        #self.speakerDiscover()

        #self.hueDiscover()
        #self.startScheduler()

    @classmethod
    def speakerDiscover(cls):
        """

        Finds all sonos speakers

        """
        #todo custom group for all speakers
        cls.voice = list(soco.discover())[0].group.coordinator


    """
    ignore for now
    @classmethod
    def hueDiscover(cls):


        bridge = Bridge()
        bridge.connect()

        cls.lights = CaseInsensitiveDict((light.name, light) for light in bridge.get_light_objects())
    """
    @classmethod
    def getVoice(cls):
        return cls.voice


    @classmethod
    def startScheduler(cls):
        print "Creating Scheduler"
        cls.scheduler = schedule.Scheduler()

    @classmethod
    def getScheduler(cls):
        return cls.scheduler

    @classmethod




    @classmethod
    def getStorage(cls):
        return cls.storage


    #Server commands

    def startServer(self):
        print "Creating Http server...."
        self.server = HttpServer(8000)
        self.server.start()

    def stopServer(self):
        self.server.stop()

    def getIp(self):
        self.ip = detect_ip_address()