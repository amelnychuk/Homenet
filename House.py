#Main dispatcher
#This will store data
#build scheduals
#Host http server

import os



class House(object):
    #maybe a singleton with http server
    #resources
    #control time
    DataDir = os.path.join(os.getcwd(), "mp3")

    def __init__(self):
        pass

    def startServer(self):
        pass

    def stopServer(self):
        pass

    def run(self):
        #start http server
        #run scheduals
        #build mp3s
        pass



class Zone(House):
    def __init__(self):
        pass

class Schedual(House):
    def __init__(self):
        pass

    def run(self):
        pass
        #set time
        #execute events


