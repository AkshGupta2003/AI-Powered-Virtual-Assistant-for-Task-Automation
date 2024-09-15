import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def authenticate_calendar():
    """Authenticates with the Google Calendar API."""
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    
    return creds

def create_event(service, event_details):
    """Creates a new event in the user's primary calendar."""
    try:
        event = service.events().insert(calendarId='primary', body=event_details).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        return event
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None
    
def delete_event(service, event_id):
    """Deletes an event from the user's primary calendar using its event ID."""
    try:
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        print(f"Event {event_id} deleted successfully.")
    except HttpError as error:
        print(f"An error occurred while deleting the event: {error}")

def update_event(service, event_id, updated_event_details):
    """Updates an event in the user's primary calendar using its event ID."""
    try:
        updated_event = service.events().update(calendarId='primary', eventId=event_id, body=updated_event_details).execute()
        print(f"Event updated: %s" % (updated_event.get('htmlLink')))
        return updated_event
    except HttpError as error:
        print(f"An error occurred while updating the event: {error}")
        return None