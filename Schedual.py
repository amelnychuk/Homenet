from House import HouseAI, Zone
from Sound import Sound
from Event import Event

import schedule
import time
from datetime import datetime, timedelta

from Calendar import GoogleCalendar

def test():
    house = HouseAI()
    house.startServer()

    s = Sound("10:30")
    s.buildMp3("Test")

    start = datetime.now()
    t = "{}:{}".format(start.hour, start.minute + 1)
    schedule.every().sunday.at(t).do(s)



    stop = 0
    while not stop:
        schedule.run_pending()
        if datetime.now().minute == start.minute + 2:
            stop = 1
    time.sleep(5)
    house.stopServer()
# TODO :: HIGHEST PRIORITY BUILD SCHEDULE, Say schedual at the beginning of the day
# TODO :: HIGH Build sound task with multiple warnings of event
# TODO :: Figure out structure of where scheduler lives inside of house.
def test():
    C = GoogleCalendar()

    S = schedule.Scheduler()
    events = C.getEventData('amelnychukoseen@gmail.com')
    print events
    for e in events:
        print e
        #build task
        ##task = Sound(e.name)
        #task.buildMp3()
        #say what the events are.

        #J = schedule.Job(1, scheduler=S)
        #J.at(e.start).do(task)

    #say how many events I have
    #if event has location get google maps location data and get time





test()
#for each event

#make a warning for beginning and next event
#announce begin/start
#annouce 25,50,75 completion if event is over 30 mins

#inherit from event?
class Announcement(Event):
    def __init__(self, time, scheduler, start=datetime.now(), end = datetime.now()):
        super(Event, self).__init__(time, start=start, end=end)
        self._scheduler = scheduler
        self.startWarning(minutes=5)
        self.startWarning(minutes=1)



    def makeSound(self):
        pass

    def startWarning(self, minutes=1):
        td = timedelta(minutes=minutes)
        starttime = self.getStart() - td
        msg = "5 minutes until {} begins".format(self.name)
        announcement = Sound(msg)
        Job = schedule.Job(interval=2, schedule = self._scheduler)
        str_time = "{}:{}".format(starttime.hour, starttime.minute)
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
