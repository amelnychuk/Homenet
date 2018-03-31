from Brain import Brain
from datetime import datetime

#Build in casting to children objects
#Build a child registry


class Event(object):
    """
    Class to process google calendar events
    """

    def __init__(self, name='None', start=datetime.now(), end=datetime.now(), index=None):
        self.setName(name)
        self._start = start
        self._end = end
        self._scheduler = Brain.getScheduler()
        self._index = index




    def getName(self):
        return self._name


    def setName(self, name):
        self._name = name


    def getStart(self, asDateTime=True):
        if asDateTime:
            return self._start
        else:
            return "{}:{}".format(self._start.hour, str(self._start.minute).zfill(2))


    def setStart(self, start):
        self._start = start


    def getEnd(self, asDateTime=True):
        if asDateTime:
            return self._end
        else:
            return "{}:{}".format(self._end.hour, str(self._end.minute).zfill(2))


    def setEnd(self, end):
        self._end = end

    def setIndex(self, idx):
        self._index = idx

    def getIndex(self):
        return self._index

    def cast(self, eventClass):
        eventClass = eventClass()
        for attr_name in self.__class__.__dict__:
            setattr(eventClass, attr_name, getattr(eventClass, attr_name))
        return eventClass

    def __str__(self):
        return "Event: {} starts at {} and ends at {}".format(self.getName(), self.getStart(asDateTime=False), self.getEnd(asDateTime=False))

    def __repr__(self):
        return "<Event:{} at {} until {}>".format(self.getName(), self.getStart(asDateTime=False), self.getEnd(asDateTime=False))



class Light(Event):

    #This will build a schedual for the hue lights
    def __init__(self, time):
        super(Light, self).__init__(time)









