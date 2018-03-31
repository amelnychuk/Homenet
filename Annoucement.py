
from Event import Event

from Sound import Sound



import schedule
import time
from datetime import datetime, timedelta



class Announcement(Event):
    def __init__(self, name='None', start=datetime.now(), end=datetime.now(), event = None):

        if isinstance(event, Event):
            super(Announcement, self).__init__(name=event.getName(),
                                               start=event.getStart(),
                                               end=event.getEnd(),
                                               index=event.getIndex())
        else:
            super(Announcement, self).__init__(name=name, start=start, end=end, index=None)


        self.announcements()



    def begin(self):
        print "begin: ", self.getName(), self._name
        msg = "It is time for {}.".format(self.getName())
        self.makeJob(msg, self.getStart())

    def warning(self, minutes):


        if minutes > 1:
            msg = "{} minutes until next event"
        else:
            msg = "{} minute until next event"
        msg = msg.format(minutes)

        td = timedelta(minutes=minutes)

        #warning until next event, last event doesn't have a next event
        if self.getIndex() != -1:
            start = self.getEnd() - td
            self.makeJob(msg, start)

        #add extra warning for the first event
        if self.getIndex() == 0:
            start = self.getStart() - td
            self.makeJob(msg, start)

    def progress(self):
        duration = self.getEnd() - self.getStart()
        if duration.seconds > 3600:
            amount = 4
            for i in range(1, amount):
                newtime = duration / int(1 / ((i + 1) / float(amount)))
                newtime = self.getStart() + newtime
                progress = i/float(amount) * 100
                msg = "{} is {} percent complete".format(self._name, int(progress))

                self.makeJob(msg, newtime)





    def makeJob(self, msg, start):

        announce = Sound(msg)
        announce.buildMp3()
        #announce()

        Job = schedule.Job(interval=1, scheduler=self._scheduler)
        Job.unit = 'days'
        str_time = "{}:{}".format(start.hour, start.minute)
        print "Starting warning at: ", str_time
        Job.at(str_time).do(announce)

    def announcements(self):
        self.begin()
        self.warning(minutes=5)
        self.warning(minutes=1)
        self.progress()

    def __str__(self):
        return "Announce: {} starts at {} and ends at {}".format(self.getName(), self.getStart(asDateTime=False), self.getEnd(asDateTime=False))

    def __repr__(self):
        return "<Announce:{} at {} until {}>".format(self.getName(), self.getStart(asDateTime=False), self.getEnd(asDateTime=False))







def eventBeginSound(name):
    return "{} has begun.".format(name)

def eventProgress(name, time):
    #percentage of time to time begin
    percentage = None
    return "It is {},{} is {} complete.".format(time,name, percentage)

def eventWarning(name, time):

    Sound( "One minute left until the end of {}".format(name))


def buildJob(name, start, end, scheduler):
    Sound(name)



def buildJobsFromCalendar():
    pass
    #get google data
    #for each event

def test():

    start  = datetime.now() + timedelta(seconds=10)
    end = start + timedelta(minutes=5)

    A = Announcement(name="Poopy",start=start, end=end)



