import os
import email
import re
import glob

def clean_email_body(text):
    # Remove signatures (basic: look for '--' or 'Best,')
    text = re.split(r'\n(--|Best,|Sincerely,|Thanks,|Regards,)', text)[0]
    # Remove quoted reply chains (lines starting with '>')
    text = re.sub(r'\n>.*', '', text)
    # Remove email footers/disclaimers (customize for your signature)
    # Add more rules as needed
    return text.strip()

folder = 'your_eml_export_folder'
for filename in glob.glob(os.path.join(folder, '*.eml')):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f)
        subject = msg.get('Subject', '')
        date = msg.get('Date', '')
        to = msg.get('To', '')
        from_ = msg.get('From', '')
        # Get body (assuming simple, single-part emails)
        if msg.is_multipart():
            body = ''
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    break
        else:
            body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')

        cleaned_body = clean_email_body(body)
        # Save/print as needed, or write to CSV/JSONL
        print(f"{date}\t{subject}\t{cleaned_body[:120]}...")  # Preview first 120 chars

