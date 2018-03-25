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
    def __init__(self, name='None', start=datetime.now(), end = datetime.now(), scheduler = None):
        super(Announcement, self).__init__(name=name, start=start, end=end)
        self._scheduler = scheduler
        for i in range(1, 3):
            self.startWarning(minutes=i)





    def makeSound(self):
        pass

    def startWarning(self, minutes=1):
        td = timedelta(minutes=minutes)
        starttime = self.getStart() + td
        msg = "5 minutes until {} begins".format(self.name)
        announcement = Sound(msg)
        announcement.buildMp3()
        Job = schedule.Job(interval=1, scheduler=self._scheduler)
        Job.unit = 'days'
        str_time = "{}:{}".format(starttime.hour, starttime.minute)
        print "Starting warning at: ", str_time
        Job.at(str_time).do(announcement)

    def progress(self):
        """
        If event is longer than one hour create progress announcement jobs for scheduler
        :return:
        """
        duration = self.getEnd(str=False) - self.getStart(str=False)
        if duration.hour > 1:
            #create time at 25,50 and 75% progress
            duration * .25
            for i in range(3):
                newtime = duration * .25 * i
                newtime = self.getStart + duration
                #make job at time





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
    S = schedule.Scheduler()
    start  = datetime.now() + timedelta(seconds=10)
    end = start + timedelta(minutes=5)

    A = Announcement(start=start, end=end, schedule=S)



