#Main dispatcher
#This will store data
#build scheduals
#Host http server

import os

import soco
from phue import Bridge

from collections import OrderedDict
import json

class MetaClass(type):
    def __init__(cls, name, bases, d):
        type.__init__(cls, name, bases, d)




class House(object):
    #maybe a singleton with http server
    #resources
    #control time


    def __init__(self):
        print "House"
        self.sonosDiscovery()
        self.hueDiscover()

    @classmethod
    def sonosDiscovery(cls):
        """
        Collects up the speakers into a dictionary
        Returns:

        """
        print "Print discovering speakers"
        sonos = list(soco.discover())
        cls.speakers = {speaker.player_name : speaker for speaker in sonos}


    @classmethod
    def hueDiscover(cls):
        """
        Gets hue lights
        Returns:

        """
        print "discovering lights"
        bridge = Bridge()
        bridge.connect()

        cls.lights = {light.name: light for light in bridge.get_light_objects()}

    @classmethod
    def getSpeakers(cls):
        return cls.speakers

    @classmethod
    def getSpeakerNames(cls):
        return cls.speakers.keys()

    @classmethod
    def getLights(cls):
        return cls.lights

    @classmethod
    def getLightNames(cls):
        return cls.lights.keys()

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
        OrderedDict.__getattr__(self,name)

    def __setattr__(self, name, value):
        if not name.startswith('_'):
            self[name] = value
        else:
            OrderedDict.__setattr__(self, name, value)

    def asJson(self):
        return json.dumps(self, indent=4)

    def load(self):
        pass

    def save(self):
        pass





    def setName(self, name):
        pass

    def _addDevice(self, devicetype ,deviceName):
        """

        Args:
            deviceName: (str) or (list of str) adds speaker names to objects

        Returns:

        """
        # TODO:: Add else on messages
        if devicetype in self.devices.keys():
            if type(deviceName) == str:
                if deviceName in House.getSpeakerNames():
                    self.devices[devicetype].append(deviceName)

            elif type(deviceName) == list:
                for dn in deviceName:
                    if type(dn) == str:
                        if dn in House.getSpeakerNames():
                            self.devices[devicetype].extend(deviceName)
                        
    def addLights(self, lightName):
        self._addDevice('lights', lightName)

    def addSpeaker(self, speakerName):
        self._addDevice('speakers', speakerName)
        


"""
    def getSpeakers(self):
        return House.getSpeakers()

    def getLights(self):
        return House.getLights()
        
"""
h = House()
#h.getSpeakers()
z = Zone('LivingRoom')
z.getSpeakers()
z.addSpeaker('Living Room')
print z.getLights()
print z

