#Main dispatcher
#This will store data
#build scheduals
#Host http server

import os

import soco
from phue import Bridge

from collections import OrderedDict
import json

class House(object):
    #maybe a singleton with http server
    #resources
    #control time


    def __init__(self):
        self.sonosDiscovery()
        self.hueDiscover()

    @classmethod
    def sonosDiscovery(cls):
        """
        Collects up the speakers into a dictionary
        Returns:

        """
        sonos = list(soco.discover())
        cls._speakers = {speaker.player_name : speaker for speaker in sonos}

    @classmethod
    def hueDiscover(cls):
        """
        Gets hue lights
        Returns:

        """
        bridge = Bridge()
        bridge.connect()

        cls._lights = {light.name: light for light in bridge.get_light_objects()}

    @classmethod
    def getSpeakers(cls):
        return cls._speakers

    @classmethod
    def getSpeakerNames(cls):
        return cls._speakers.keys()

    def startServer(self):
        pass

    def stopServer(self):
        pass

    @classmethod
    def setStorage(cls):
        cls.storage = os.path.join(os.getcwd(), "mp3")

    @classmethod
    def getStorage(cls):
        return cls.storage

    def run(self):
        #start http server
        #run scheduals
        #build mp3s
        pass



class Zone(OrderedDict, House):
    """
    This has a collection of light and speaker names. Easily converts json files.
    """

    # TODO:: finish up structure of zones

    def __init__(self, name):
        super(Zone, self).__init__()
        self['name'] = name

        self.devices = {'lights': [],
        'speakers': []}

    def __getattr__(self, name):
        if not name.startswith('_'):
            return self[name]
        super(Zone, self).__getattr__(name)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self[name] = value
        else:
            super(Zone, self).__setattr__(name, value)

    def asJson(self):
        return json.dumps(self, indent=4)

    def load(self):
        pass

    def save(self):
        pass





    def setName(self, name):
        pass

    def addSpeakers(self, speakerName):
        """

        Args:
            speakerName: (str) or (list of str) adds speaker names to objects

        Returns:

        """
        if type(speakerName) == str:
            if speakerName in House.getSpeakerNames():
                self.devices['speakers'].append(speakerName)
        elif type(speakerName) == list:

            for speaker in speakerName:
                if type(speaker) == str:
                    if speakerName in House.getSpeakerNames():
                        self.devices['speakers'].extend(speakerName)



    def getSpeakers(self):
        pass

    def getLights(self):
        pass


class Schedual(House):
    def __init__(self):
        pass

    def run(self):
        pass
        #set time
        #execute events


