import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path

# If modifying these scopes, delete the file email_token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate_gmail():
    """Authenticates the Gmail API."""
    creds = None
    if os.path.exists('email_token.json'):
        creds = Credentials.from_authorized_user_file('email_token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('email_credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('email_token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def create_email(sender, recipient, subject, body):
    """Creates an email message."""
    message = MIMEText(body)
    message['to'] = recipient
    message['from'] =  sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(service, user_id, email_message):
    """Sends an email using the Gmail API."""
    try:
        message = service.users().messages().send(userId=user_id, body=email_message).execute()
        print(f"Email sent successfully: {message['id']}")
        return message
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# def emailer_task(sender, recipient, subject, body):
#     """The task function for sending an email."""
#     # Authenticate Gmail API
#     creds = authenticate_gmail()
#     service = build('gmail', 'v1', credentials=creds)

#     # Create email
#     email_message = create_email(sender, recipient, subject, body)

#     # Send email
#     send_email(service, 'me', email_message)
