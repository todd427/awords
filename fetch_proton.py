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
import getpass


from dotenv import load_dotenv
import argparse
import imaplib
import email
import json

# Load .env file automatically (defaults to ".env" in current dir)
load_dotenv()

def get_creds(args):
    creds = {
        "IMAP_HOST": args.imap_host or os.getenv("PROTON_IMAP_HOST", "127.0.0.1"),
        "IMAP_PORT": args.imap_port or os.getenv("PROTON_IMAP_PORT", "1143"),
        "USERNAME": args.user or os.getenv("PROTON_USER"),
        "PASSWORD": args.password or os.getenv("PROTON_PASSWORD"),
    }

    # Fallback to prompt if not found
    if not creds["USERNAME"]:
        creds["USERNAME"] = input("ProtonMail username: ")
    if not creds["PASSWORD"]:
        import getpass
        creds["PASSWORD"] = getpass.getpass("ProtonMail password: ")

    return creds

# ... [rest of your script, using get_creds as before] ...
ment("--imap-port", type=str, default=None, help="IMAP port (default 1143)")
    parser.add_argument("--output", type=str, default="proton_sent.json", help="Output JSON path")
    parser.add_argument("--folder", type=str, default="Sent", help="IMAP folder to fetch from")
    parser.add_argument("--limit", type=int, default=500, help="Max number of emails to fetch")
    parser.add_argument("--dry-run", action="store_true", help="Only show subjects, don't save")

    args = parser.parse_args()
    creds = get_creds(args)
    messages = fetch_sent_emails(creds, folder=args.folder, dry_run=args.dry_run, limit=args.limit)

    if not args.dry_run:
        save_to_json(messages, args.output)
