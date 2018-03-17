from House import HouseAI, Zone
from Sound import Sound

import schedule
import time
import datetime

from Calendar import GoogleCalendar

def test():
    house = HouseAI()
    house.startServer()

    s = Sound("10:30")
    s.buildMp3("Test")

    start = datetime.datetime.now()
    t = "{}:{}".format(start.hour, start.minute + 1)
    schedule.every().sunday.at(t).do(s)



    stop = 0
    while not stop:
        schedule.run_pending()
        if datetime.datetime.now().minute == start.minute + 2:
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
def eventBeginSound(name):
    return "{} has begun.".format(name)

def eventProgress(name, time):
    #percentage of time to time begin
    percentage = None
    return "It is {},{} is {} complete.".format(time,name, percentage)

def eventWarning(name, time):
    return "One minute left until the end of {}".format(name)

def buildJob(name, start, end, scheduler):
    Sound(name)



def buildJobsFromCalendar():
    pass
    #get google data
    #for each event
