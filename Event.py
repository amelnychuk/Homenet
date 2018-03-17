
from datetime import datetime

class Event():
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

    @property
    def start(self):
        return "{}:{}".format(self._start.hour, str(self._start.minute).zfill(2))


    @start.setter
    def start(self, start):
        self._start = start

    @property
    def end(self):
        return "{}:{}".format(self._end.hour, str(self._end.minute).zfill(2))

    @end.setter
    def end(self, end):
        self._end = end

    def __str__(self):
        return "Poopy"

    def __repr__(self):
        return "<Event:{} at {} until {}>".format(self.name, self.start, self.end)



class Light(Event):

    #This will build a schedual for the hue lights
    def __init__(self, time):
        super(Light, self).__init__(time)









