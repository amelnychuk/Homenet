
from datetime import datetime

class Event(object):
    """
    Class to process google calendar events
    """

    def __init__(self, name='None', start=datetime.now(), end = datetime.now()):
        self._name = name
        self._start = start
        self._end = end

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


    def getStart(self, str=False):
        if str:
            return "{}:{}".format(self._start.hour, str(self._start.minute).zfill(2))
        else:
            return self._start


    def setStart(self, start):
        self._start = start


    def getEnd(self, str=False):
        if str:
            return "{}:{}".format(self._end.hour, str(self._end.minute).zfill(2))
        else:
            return self._end


    def setEnd(self, end):
        self._end = end

    def __str__(self):
        return "Event: {} starts at {} and ends at {}".format(self.name, self.getStart(str=True), self.getEnd(str=True))

    def __repr__(self):
        return "<Event:{} at {} until {}>".format(self.name, self.getStart(str=True), self.getEnd(str=True))



class Light(Event):

    #This will build a schedual for the hue lights
    def __init__(self, time):
        super(Light, self).__init__(time)









