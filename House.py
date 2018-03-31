#Main dispatcher
#This will store data
#build scheduals
#Host http server

import os




from Brain import Brain

from Calendar import GoogleCalendar
import schedule
from Annoucement import Announcement




class HouseAI(Brain):
    """
    Class to run api calls, build event objects, and run schedules
    """




    def __init__(self):
        super(HouseAI, self).__init__()
        print "Initializing House AI"
        #these might be sets
        #list of zones
        self.zones = []
        #list of events
        self.scheds = []


        self.startCalendar()


        #start server
        self.startServer()

        #dictionary of sound objects
        self.announcements = {}

        #dictionary of events
        self._events = {}

    def calendarEventsToReminders(self):
        job = schedule.Job(interval=2, scheduler=self.Schedule)
        job.at("6:50").do(self.getRoutine)

    def morningRoutine(self):
        self.announceEvents()






    def announceEvents(self):

        self.Calendar.getEventData('Routine')
        events = self.Calendar.getEvents('Routine')
        for i, evt in enumerate(events):
            A = Announcement(event=evt)
            if i == len(self.Calendar.getEvents('Routine')) - 1:
                A.setIndex(-1)

    def runSchedule(self):
        ##todo::run every week day
        Job = schedule.Job(interval=1, scheduler=self.getScheduler())
        Job.unit = 'days'
        Job.at("06:45").do(self.morningRoutine)

    #schedule commands



    #Calendar commands

    def startCalendar(self):
        print "Getting google calendar"
        self.Calendar = GoogleCalendar()





    @classmethod
    def getSpeakers(cls):
        return cls.speakers

    @classmethod
    def getSpeakerNames(cls):
        return cls.speakers.keys()

    @classmethod
    def getLights(cls):
        return cls.lights

    @classmethod
    def getLightNames(cls):
        return cls.lights.keys()








        


