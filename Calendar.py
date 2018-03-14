#from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
from dateutil.parser import parse
from dateutil import tz
import pytz

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'CalandarLights'

class Calendar(object):
    def __init__(self):
        self.setCalendarService()
        self.setCalendarIDs()
        self.setTimesOfDay()

    def setCalendarService(self):
        """Builds a google calendar service from

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, 'credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'client_secret.json')

        store = Storage(credential_path)
        print (store)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)


        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=http)


    def setCalendarIDs(self):
        """
        Function to get different calendars
        Args:
            service: Google calendar api service

        Returns: (dict) of calendar name mapped to calendar id

        """

        page_token = None
        calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
        self.calendarIDS= {item['summary']: item['id'] for item in calendar_list.get('items', [])}


    def getEventData(self, calendarName):
        """
        Gets the events from your calendar.
        Args:
            calendar_id:  Google calendar id

        Returns:

        """
        try:
            calendar_id = self.calendarIDS[calendarName]
        except KeyError:
            print "Calendars are: "
            print self.calendarIDS.keys()
            return None

        events = self.service.events().list(
            calendarId=calendar_id,
            timeMin=self.day_begin,
            timeMax=self.day_end,
            singleEvents=True,
            timeZone="America/Los_Angeles",
            orderBy='startTime').execute().get('items', [])

        for event in events:
            start = parse(event['start']['dateTime'])
            end = parse(event['end']['dateTime'])
            print event['summary'], event['start']['dateTime'], event['end']['dateTime']
            # print "parsedDate",  datetime.datetime.strptime(start,"%Y-%m-%dT%H:%M:%S")
            sh, sm = start.hour, start.minute
            eh, em = end.hour, end.minute
            print "parsed: ", sh, sm, eh, em
            # print "converted datetime", timezone.localize(datetime.datetime(event['start']['dateTime']))

    def setTimesOfDay(self):
        # TODO:: PRIORITY convert local start and end of day to utc
        """
        Day end and begin need in universal time
        Returns: beginning of day and end of day

        """
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz('America/Los_Angeles')
        day_begin = datetime.datetime.utcnow()  # 'Z' indicates UTC time
        print parse(day_begin).astimezone(to_zone)

        day_begin = day_begin.replace(hour=0, minute=0, second=0).isoformat() + 'Z'

        day_end = datetime.datetime.utcnow()

        day_end = day_end.replace(hour=23, minute=59, second=59)
        day_end = day_end.isoformat() + 'Z'

        self.day_begin = day_begin
        self.day_end = day_end


    def getEventColors(self):
        eventcolors = self.service.colors().get().execute().get('event')
        return eventcolors



C = Calendar()
#C.getEventData('Routines')
