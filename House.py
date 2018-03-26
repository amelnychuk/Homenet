#Main dispatcher
#This will store data
#build scheduals
#Host http server

import os




from Brain import Brain

from Calendar import GoogleCalendar
import schedule




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



    def eventConvert(self):

        jobs = []
        self.Sounds = {}
        for routine in self.routines:

            announcement = Sound(routine.name)

            Sound = self.announcements.setdefault(routine.name, announcement)

            job = schedule.Job(inteval=2, scheduler=self.Schedule)
            job.at(routine.start).do(self.announcements[routine.name])




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





    def run(self):
        #start http server
        #run scheduals
        #build mp3s
        pass






        


