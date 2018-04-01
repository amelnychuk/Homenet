

from House import HouseAI
from Annoucement import Announcement

from datetime import datetime, timedelta
import pytz
import time




def main():
    ## TODO: Convert
    print "starting House"
    House = HouseAI()
    #House.getRoutine(name='amelnychukoseen@gmail.com')
    House.Calendar.getEventData('Routine')
    ed = House.Calendar.getEvents('Routine')
    print ed
    if ed:
        for e in ed:



            if e.getStart() > datetime.utcnow().replace(tzinfo=pytz.UTC):
                print e.getName()
                print "start: ", e.getStart()
                print "now: ", datetime.utcnow().replace(tzinfo=pytz.UTC)

                Announcement(event=e)

        stoptime = datetime.now() + timedelta(hours=2)
        while datetime.now() < stoptime:
            House.getScheduler().run_pending()
    else:
        print "No Jobs"



    #todo convert to announcements and build
    #todo build job to collect information every day
    #todo run this on different computer

    print
    #Todo :: fix initializeing of events to build annoucement jobs

    House.stopServer()

    #start  = datetime.now() + timedelta(seconds=10)
    #end = start + timedelta(minutes=5)
"""
    A = Announcement(name="MyTest", start=start, end=end, scheduler=House.schedule)
    stop = 0
    while not stop:
        House.schedule.run_pending()
        if datetime.now().minute == A.getEnd(str=False).minute + 2:
            stop = 1
    time.sleep(5)

    print "Stoping server..."
    House.stopServer()

    #House.addZone(livingRoom())
    # todo:: add scheduler for events
    # todo:: schedule collection of google calendar events
"""



    #print House.getSpeakerNames()
    #print House.getLightNames()



if __name__ == '__main__':
    main()
