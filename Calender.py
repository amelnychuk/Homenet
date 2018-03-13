#from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
from dateutil.parser import parse
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


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

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

    return credentials


# TODO:: clean this function up
def getEventData():

    #getCredentials
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    page_token = None

    calendar_list = service.calendarList().list(pageToken=page_token).execute()
    calendar_id = None
    for item in calendar_list.get('items', []):
        if item['summary'] == 'Routine':
            calendar_id = item['id']
    #calendar_list_entry = service.calendarList().get(calendarId='pcjici38do0gmr4pg4n6hb2u10@group.calendar.google.com').execute()
    #print calendar_list_entry
    now = datetime.datetime.now()  # 'Z' indicates UTC time
    now = now.replace(hour=0, minute=0, second=0).isoformat() + 'Z'
    print "now: ", now
    #getDayEvents
    d = datetime.datetime.utcnow()
    #d = d.replace(day=datetime.datetime.now().day+2)
    d = d.replace(hour=11, minute=59, second=59)
    tommorow = d.isoformat() + 'Z'
    #tommorow = datetime.datetime.now().replace(day=datetime.datetime.now().day+2).utcnow().isoformat() + 'Z'
    print "tommorow: ", tommorow
    eventsResult = service.events().list(
        calendarId=calendar_id, timeMin=now, timeMax=tommorow,singleEvents=True,timeZone="America/Los_Angeles",orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    print events
    #get event colors
    eventcolors = service.colors().get().execute().get('event')
    print events
    timezone = pytz.timezone('America/Los_Angeles')

    for event in events:
        start = parse(event['start']['dateTime'])
        end = parse(event['end']['dateTime'])
        print event['summary'], event['start']['dateTime'], event['end']['dateTime']
        #print "parsedDate",  datetime.datetime.strptime(start,"%Y-%m-%dT%H:%M:%S")
        sh, sm = start.hour, start.minute
        eh, em = end.hour, end.minute
        print "parsed: ", sh,sm,eh,em
        #print "converted datetime", timezone.localize(datetime.datetime(event['start']['dateTime']))

print getEventData()