#build color converter here.
import numpy as np

class Color():
    """
    Inits with 0-1
    """
    def __init__(self, r,g,b):
        self._rgb = np.array([r,g,b])
    @property
    def r(self):
        return self._rgb[0]
    @property
    def g(self):
        return self._rgb[1]
    @property
    def b(self):
        return self._rgb[2]

    def asCt(self):
        """

        :returns: rgb values as CIE 1931
        """
        _sum = np.sum(self._rgb)
        return [self.r / _sum,  self.g / _sum]



