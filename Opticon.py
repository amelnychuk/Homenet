

from House import HouseAI, Zone


def livingRoom():
    livingRoom = Zone("Living Room")
    print livingRoom.asJson()
    return livingRoom


def main():
    print "starting House"
    House = HouseAI()
    House.addZone(livingRoom())
    # todo:: add scheduler for events

    print House.getSpeakerNames()
    print House.getLightNames()



if __name__ == '__main__':
    main()
