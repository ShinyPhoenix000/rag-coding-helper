# Gmail API in Python

## Installation

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Authentication

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project and enable Gmail API
3. Create OAuth 2.0 credentials and download `credentials.json`

```python
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('gmail', 'v1', credentials=creds)
```

## Listing Messages
```python
results = service.users().messages().list(userId='me', maxResults=10).execute()
messages = results.get('messages', [])
for msg in messages:
    print(msg['id'])
```

## Reading a Message
```python
msg_id = messages[0]['id']
msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
print(msg)
```

## Sending a Message
```python
import base64
from email.mime.text import MIMEText

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

message = create_message('me', 'to@example.com', 'Subject', 'Hello!')
send_message = service.users().messages().send(userId='me', body=message).execute()
print(send_message)
```

## References
- [Gmail API Python Quickstart](https://developers.google.com/gmail/api/quickstart/python)
- [Gmail API Docs](https://developers.google.com/gmail/api)
