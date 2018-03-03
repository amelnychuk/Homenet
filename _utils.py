#build color converter here.
import numpy as np

class Color():


    def __init__(self, *args):
        if len(args) == 3:
            self._rgb = np.array([args[0], args[1], args[2]])

        if len(args) == 1:
            if args[0].startswith("#"):
                self.setHex(args[0])
    @property
    def r(self):
        return self._rgb[0]
    @property
    def g(self):
        return self._rgb[1]
    @property
    def b(self):
        return self._rgb[2]

    def setHex(self, hexCode):
        hexCode = hexCode.lstrip('#')
        self._hex = hexCode
        self._rgb = [int(hexCode[i:i+2], 16)/255.0 for i in (0, 2 ,4)]



    def asCt(self):
        """

        :returns: rgb values as CIE 1931
        """
        _sum = np.sum(self._rgb)
        return [self.r / _sum,  self.g / _sum]






