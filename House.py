#Main dispatcher
#This will store data
#build scheduals
#Host http server

import os

import soco
from phue import Bridge

class House(object):
    #maybe a singleton with http server
    #resources
    #control time


    def __init__(self):
        self.sonosDiscovery()
        self.hueDiscover()

    def sonosDiscovery(self):
        """
        Collects up the speakers into a dictionary
        Returns:

        """
        sonos = list(soco.discover())
        self._speakers = {speaker.player_name : speaker for speaker in sonos}

    def hueDiscover(self):
        """
        Gets hue lights
        Returns:

        """
        bridge = Bridge()
        bridge.connect()

        self._lights = {light.name: light for light in bridge.get_light_objects()}

    def getSpeakers(self):
        return self._speakers

    def getSpeakerNames(self):
        return self._speakers.keys()

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



class Zone(House):
    """
    This has a collection of light and speaker names. Can load from Json config file.
    """
    def __init__(self, name):
        self._name = name
        self._lights = []
        self._speakers = []

    def addSpeakers(self, speakerName):
        """

        Args:
            speakerName: (str) or (list of str) adds speaker names to objects

        Returns:

        """
        if type(speakerName) == str:
            self._speakers.append(speakerName)
        else:
            self._speakers.extend(speakerName)

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


