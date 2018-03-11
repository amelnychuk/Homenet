#Main dispatcher
#This will store data
#build scheduals
#Host http server

import os

import soco
from phue import Bridge
from Server import HttpServer, detect_ip_address



import json

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

class Brain(object):
    """
    Collects up all the devices in the home.
    """
    # TODO :: generalize data structure to handle all different types of devices
    def __init__(self):
        print "Discover"
        self.speakerDiscover()
        self.hueDiscover()

    @classmethod
    def speakerDiscover(cls):
        """

        Finds all sonos speakers

        """
        # TODO:: send a message to the speakers to verify
        cls.voice = list(soco.discover())[0].group.coordinator

        #cls.speakers = {speaker.player_name: speaker for speaker in list(soco.discover())}

    @classmethod
    def hueDiscover(cls):
        """
        Gets hue lights

        """

        bridge = Bridge()
        bridge.connect()
        # TODO :: Varification of lights
        cls.lights = CaseInsensitiveDict((light.name, light) for light in bridge.get_light_objects())



class HouseAI(Brain):
    #maybe a singleton with http server
    #resources
    #control time


    # TODO:: Create a metaclass to register created zones
    # TODO:: Auto load zone files
    # TODO:: Start HTTPS Server
    # TODO:: Scoop up schedual from google calendar

    def __init__(self):
        super(HouseAI, self).__init__()
        print "House"
        #these might be sets
        #list of zones
        self.zones = []
        #list of events
        self.scheds = []
        self.setStorage()

    @classmethod
    def getVoice(self):
        return self.voice

    def startServer(self):
        self.server = HttpServer(8000)
        self.server.start()

    def stopServer(self):
        self.server.stop()

    def getIp(self):
        self.ip = detect_ip_address()


    def addZone(self, zone):
        self.zones.append(zone)


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



    @classmethod
    def setStorage(cls):
        path = os.path.join(os.getcwd(), "mp3")
        if os.path.isdir(path):
            cls.storage = path
        else:
            os.makedirs(path)
            cls.storage = path

    @classmethod
    def getStorage(cls):
        return cls.storage

    def run(self):
        #start http server
        #run scheduals
        #build mp3s
        pass



class Zone(HouseAI):
    """
    This has a collection of light and speaker names. Easily converts and loads json files.
    """

    # TODO:: finish up structure of zones

    def __init__(self, name):
        #super(Zone, self).__init__()

        self.data = {}

        self.data['name'] = name
        self.data['devices'] = {'lights': [],
        'speakers': []}

        #self.autoLoad()



    def asJson(self):
        return json.dumps(self.data, indent=4)

    def load(self):
        pass

    def save(self):
        pass

    @property
    def speakers(self):
        return self.data['devices']['speakers']


    def setName(self, name):
        pass

    def getName(self):
        return self.data['name']

    def _addDevice(self, devicetype ,deviceName):
        """

        Args:
            deviceName: (str) or (list of str) adds speaker names to objects

        Returns:

        """
        # TODO:: Add else on messages
        deviceName = deviceName.lower().replace(" ", "")
        if devicetype in self.data['devices'].keys():
            if type(deviceName) == str:
                if deviceName in HouseAI.getSpeakerNames():
                    self.data['devices'][devicetype].append(deviceName)

            elif type(deviceName) == list:
                for dn in deviceName:
                    if type(dn) == str:
                        if dn in HouseAI.getSpeakerNames():
                            self.data['devices'][devicetype].extend(deviceName)
                        
    def addLight(self, lightName):
        self._addDevice('lights', lightName)

    def addSpeaker(self, speakerName):
        self._addDevice('speakers', speakerName)

    def autoLoad(self):
        print "autoloading"
        #todo :: handle multiple speakers and lights of multiple names
        self.addSpeaker( self.getName())
        self.addLight( self.getName())


        


