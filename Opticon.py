

from House import HouseAI
from Annoucement import Announcement

from datetime import datetime, timedelta
import time




def main():
    print "starting House"
    House = HouseAI()
    #House.getRoutine(name='amelnychukoseen@gmail.com')
    ed = House.Calendar.getEventData('amelnychukoseen@gmail.com')
    print ed
    print type(ed[0].getStart())
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
