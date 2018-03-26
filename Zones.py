from House import HouseAI

import json

class Zone(HouseAI):
    """
    This has a collection of light and speaker names. Easily converts and loads json files.
    """

    def __init__(self, name):
        # super(Zone, self).__init__()

        self.data = {}

        self.data['name'] = name
        self.data['devices'] = {'lights': [],
                                'speakers': []}

        # self.autoLoad()

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

    def _addDevice(self, devicetype, deviceName):
        """

        Args:
            deviceName: (str) or (list of str) adds speaker names to objects

        Returns:

        """

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
        self.addSpeaker(self.getName())
        self.addLight(self.getName())