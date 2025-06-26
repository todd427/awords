# fetch_gmail.py
# This script fetches sent messages from Gmail and saves them to a JSON file.
# It uses the Google Gmail API to authenticate and fetch the messages.
# The script requires the following dependencies:
# - google-api-python-client
# - google-auth-oauthlib
# - beautifulsoup4
# - argparse

import os
import json
import base64
import argparse
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pathlib import Path


# Scope to read Gmail messages
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            CREDENTIALS_PATH = Path(__file__).resolve().parent.parent / "config" / "credentials.json"
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)

            # Use manual browser flow
            creds = flow.run_local_server(port=0, open_browser=True)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def get_sent_messages(service, max_messages):
    results = service.users().messages().list(userId='me', labelIds=['SENT'], maxResults=max_messages).execute()
    messages = results.get('messages', [])
    return messages

def extract_message(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    headers = msg['payload'].get('headers', [])
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")

    # Traverse parts
    def get_text(payload):
        if 'parts' in payload:
            for part in payload['parts']:
                result = get_text(part)
                if result:
                    return result
        elif payload.get('mimeType') == 'text/plain':
            return base64.urlsafe_b64decode(payload['body'].get('data', '')).decode('utf-8', errors='ignore')
        elif payload.get('mimeType') == 'text/html':
            html = base64.urlsafe_b64decode(payload['body'].get('data', '')).decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            return soup.get_text()
        return ""

    body = get_text(msg['payload']) or "(No Content)"
    return {
        'id': msg_id,
        'subject': subject.strip(),
        'body': body.strip()
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str, default='sent_messages.json', help='Output JSON file')
    parser.add_argument('--limit', type=int, default=100, help='Number of messages to fetch')
    args = parser.parse_args()

    print("Authenticating with Gmail...")
    gmail_service = authenticate_gmail()

    print(f"Fetching up to {args.limit} sent messages...")
    message_ids = get_sent_messages(gmail_service, args.limit)

    messages = []
    for msg in message_ids:
        try:
            parsed = extract_message(gmail_service, msg['id'])
            messages.append(parsed)
        except Exception as e:
            print(f"Error reading message {msg['id']}: {e}")

    with open(args.output, 'w') as f:
        json.dump(messages, f, indent=2)

    print(f"\n✅ Saved {len(messages)} messages to {args.output}")

if __name__ == '__main__':
    main()
