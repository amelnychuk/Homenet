import os
import re

from Brain import Brain
from Server import detect_ip_address

from gtts import gTTS

import time

class Sound(object):
    """
    Builds an alarm for sonos
    """
    def __init__(self, message):
        self.msg = message
        self.setVolume(50)


    def setVolume(self, vol):

        self.volume = vol




    def buildMp3(self):
        """

        Args:
            msg: (str) converts text to mp3 and saves it to disk

        Returns:

        """



        filepath = os.path.join(Brain.storage, "Notifications")
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        filename = "{0}.mp3".format(self.msg).replace(" ", "")
        pattern = re.compile('[\W_]+')
        pattern.sub('', filename)

        if not os.path.isdir(filepath):
            os.makedirs(filepath)

        outpath = os.path.join(filepath, filename)

        if not os.path.isfile(outpath):
            speech = gTTS(text=self.msg, lang='en', slow=False)
            speech.save(savefile=outpath)

        self.soundFile = filename

    def play_file(self, port=8000):
        netpath = 'http://{}:{}/{}'.format(detect_ip_address(), port, self.soundFile)
        print("netpath: ", netpath)

        z = Brain.voice
        z.volume = self.volume
        z.play_uri(uri=netpath)
        time.sleep(3)

    def __call__(self):
        self.buildMp3()
        self.play_file()