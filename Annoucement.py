
from Event import Event

from Sound import Sound


import schedule
import time
from datetime import datetime, timedelta


#for each event

#make a warning for beginning and next event
#announce begin/start
#annouce 25,50,75 completion if event is over 30 mins

#inherit from event?
class Announcement(Event):
    def __init__(self, name='None', start=datetime.now(), end = datetime.now(), EventObj = None):

        if isinstance(EventObj, Event):
            super(Announcement, self).__init__(name=EventObj.name, start=EventObj.getStart(), end=EventObj.getEnd())
        else:
            super(Announcement, self).__init__(name=name, start=start, end=end)

        self.announcements()



    def begin(self):
        msg = "Human, it is time to begin {}.".format(self.name)
        self.makeJob(msg, self.getStart())

    def warning(self, minutes):


        if minutes > 1:
            msg = "{} minute until next event."
        else:
            msg = "{} minutes until next event"
        msg.format(minutes)

        td = timedelta(minutes=minutes)
        start = self.getEnd() - td

        self.makeJob(msg, start)

    def progress(self):
        duration = self.getEnd() - self.getStart()
        if duration.hour > 1:
            amount = 10
            for i in range(amount):
                newtime = duration * (i / float(amount))
                newtime = self.getStart() + newtime

                msg = "{} is {} percent complete".format(self.name, (i/float(amount)) * 100)

                self.makeJob(msg, newtime)




    def makeJob(self, msg, start):

        announce = Sound(msg)
        announce.buildMp3()

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



