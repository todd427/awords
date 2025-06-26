# fetch_proton.py
# This script fetches sent messages from Proton Mail and saves them to a JSON file.
# It uses the Proton Bridge IMAP server to authenticate and fetch the messages.
# The script requires the following dependencies:
# - imaplib
# - email
# - json
# - argparse

import imaplib
import email
import json
import argparse
from pathlib import Path

def load_credentials(path):
    try:
        with open(path, "r") as f:
            data = f.read().splitlines()
            return dict(line.split("=", 1) for line in data if "=" in line)
    except Exception as e:
        raise RuntimeError(f"Failed to read credentials from {path}: {e}")

def fetch_sent_emails(creds, folder="Sent", dry_run=False, limit=500):
    emails = []
    try:
        mail = imaplib.IMAP4(creds["IMAP_HOST"], int(creds["IMAP_PORT"]))
        mail.login(creds["USERNAME"], creds["PASSWORD"])
        mail.select(f'"{folder}"')

        status, messages = mail.search(None, "ALL")
        if status != "OK":
            raise Exception("Search failed.")

        email_ids = messages[0].split()[-limit:]
        for num in email_ids:
            status, data = mail.fetch(num, "(RFC822)")
            if status != "OK":
                continue
            msg = email.message_from_bytes(data[0][1])
            subject = msg.get("Subject", "")
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            if dry_run:
                print(f"📧 Subject: {subject[:60]}...")
            else:
                emails.append({
                    "subject": subject,
                    "body": body,
                    "from": msg.get("From"),
                    "to": msg.get("To"),
                    "date": msg.get("Date")
                })

        mail.logout()
    except Exception as e:
        print(f"❌ Error: {e}")
    return emails

def save_to_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Saved {len(data)} messages to {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch sent Proton Mail messages via Bridge.")
    parser.add_argument("--config", type=str, default="../config/proton.cred", help="Path to credentials file")
    parser.add_argument("--output", type=str, default="proton_sent.json", help="Output JSON path")
    parser.add_argument("--folder", type=str, default="Sent", help="IMAP folder to fetch from")
    parser.add_argument("--limit", type=int, default=500, help="Max number of emails to fetch")
    parser.add_argument("--dry-run", action="store_true", help="Only show subjects, don't save")

    args = parser.parse_args()
    creds = load_credentials(args.config)
    messages = fetch_sent_emails(creds, folder=args.folder, dry_run=args.dry_run, limit=args.limit)

    if not args.dry_run:
        save_to_json(messages, args.output)
