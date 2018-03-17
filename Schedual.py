from House import HouseAI, Zone
from Event import Sound

import schedule
import time
import datetime

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