#from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from datetime import datetime, timedelta
from dateutil.parser import parse

from Event import Event


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

class GoogleCalendar(object):
    """
    Calendar object to retrieve google calendar data
    """
    def __init__(self):
        self._setCalendarService()
        self._setCalendarIDs()
        self._setTimesOfDay()


    def _setCalendarService(self):
        """Builds a google calendar service.
        Make sure your client_secret is in the same folder as this python file.

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


    def _setCalendarIDs(self):
        """
        Function to get different calendars
        Args:
            service: Google calendar api service

        Returns: (dict) of calendar name mapped to calendar id

        """

        page_token = None
        calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
        self.calendarIDS= {item['summary']: item['id'] for item in calendar_list.get('items', [])}



    def _setTimesOfDay(self):
        """
        Day end and begin need in universal time
        Returns: beginning of day and end of day

        querey format = 2018-03-14T17:00:00.000007Z
        """
        d_time = datetime.utcnow() - datetime.now()
        today = datetime.now().date()  # 'Z' indicates UTC time
        today = datetime(today.year, today.month, today.day, hour=0, minute=0, second=0)

        #start of day
        start = today + d_time
        #end of day
        end = start + timedelta(.99)

        self.day_begin = start.isoformat() + 'Z'
        self.day_end = end.isoformat() + 'Z'

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
            return []

        events = self.service.events().list(
            calendarId=calendar_id,
            timeMin=self.day_begin,
            timeMax=self.day_end,
            singleEvents=True,
            timeZone="America/Los_Angeles",
            orderBy='startTime').execute().get('items', [])


        return [Event(name=event['summary'],
                      start=parse(event['start']['dateTime']),
                      end=parse(event['end']['dateTime'])) for event in events]



    def getEventColors(self):
        """

        Returns: Google event color palete

        """
        eventcolors = self.service.colors().get().execute().get('event')
        return eventcolors


