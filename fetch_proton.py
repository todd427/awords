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
from email.header import decode_header
from decouple import config
import os

# Load configuration from .env
IMAP_HOST = config("PROTON_IMAP_HOST", default="127.0.0.1")
IMAP_PORT = config("PROTON_IMAP_PORT", cast=int, default=1143)
EMAIL_ACCOUNT = config("PROTON_USER")
EMAIL_PASSWORD = config("PROTON_PASSWORD")
OUTPUT_FILE = config("PROTON_OUTPUT_FILE", default="proton_sent.json")

def decode_mime_words(s):
    if not s:
        return ""
    decoded = decode_header(s)
    return ''.join(
        str(t[0], t[1] or 'utf-8') if isinstance(t[0], bytes) else str(t[0])
        for t in decoded
    )

def fetch_sent_emails():
    try:
        mail = imaplib.IMAP4(IMAP_HOST, IMAP_PORT)
        mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
        mail.select('"Sent"')

        result, data = mail.search(None, "ALL")
        if result != "OK":
            print("❌ Failed to search mailbox.")
            return []

        message_ids = data[0].split()
        messages = []

        for num in message_ids:
            result, data = mail.fetch(num, "(RFC822)")
            if result != "OK":
                continue

            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = decode_mime_words(msg.get("Subject", ""))
            date = msg.get("Date")
            from_ = decode_mime_words(msg.get("From", ""))
            to = decode_mime_words(msg.get("To", ""))

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        charset = part.get_content_charset() or "utf-8"
                        body = part.get_payload(decode=True).decode(charset, errors="replace")
                        break
            else:
                charset = msg.get_content_charset() or "utf-8"
                body = msg.get_payload(decode=True).decode(charset, errors="replace")

            messages.append({
                "subject": subject,
                "date": date,
                "from": from_,
                "to": to,
                "body": body.strip(),
            })

        mail.logout()
        return messages

    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def main():
    print("📨 Connecting to Proton Mail Bridge IMAP...")
    messages = fetch_sent_emails()

    if messages:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved {len(messages)} messages to {OUTPUT_FILE}")
    else:
        print("⚠️ No messages found or connection failed.")

if __name__ == "__main__":
    main()
