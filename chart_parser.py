# chart_parser.py
import json
import argparse
import os

def load_conversations(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    else:
        return data.get("conversations", [])


def clean_message(text):
    if not text:
        return ""
    # Add more cleaning steps if you want
    if isinstance(text, dict):
        # Try to extract "text" field — or skip
        text = text.get("text", "")
    elif not isinstance(text, str):
        text = ""

        text = text.replace("\r\n", "\n").replace("\r", "\n").strip()
        return text
    return text

def extract_user_messages(conversations, user_role="user"):
    all_messages = []
    conv_messages = []

    for idx, conv in enumerate(conversations):
        conv_id = f"conv_{idx+1:03d}"
        messages = []
        for msg in conv.get("mapping", {}).values():
            message = msg.get("message") if msg else None
            if not message or not message.get("content"):
                continue  # skip invalid or empty message
            content = message.get("content", {})
            if msg.get("message", {}).get("author", {}).get("role") == user_role:
                parts = content.get("parts", [])
                if parts:
                    for part in parts:
                        cleaned = clean_message(part)
                        if cleaned:
                            messages.append(cleaned)
                            all_messages.append(cleaned)
        conv_messages.append((conv_id, messages))
    return all_messages, conv_messages

def save_all_messages(all_messages, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for msg in all_messages:
            f.write(msg + "\n\n")

def save_split_conversations(conv_messages, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for conv_id, messages in conv_messages:
        out_path = os.path.join(output_dir, f"{conv_id}.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            for msg in messages:
                f.write(msg + "\n\n")

def main():
    parser = argparse.ArgumentParser(description="Parse ChatGPT conversations.json and extract user messages.")
    parser.add_argument("--input", required=True, help="Path to conversations.json")
    parser.add_argument("--output", default="output/all_chats.txt", help="Path for combined output text file")
    parser.add_argument("--split", action="store_true", help="Also split into one file per conversation")
    parser.add_argument("--split_dir", default="output/conversations", help="Directory for split conversation files")
    parser.add_argument("--user_role", default="user", help="Role to extract (default is 'user')")
    args = parser.parse_args()

    print("Loading conversations...")
    conversations = load_conversations(args.input)
    print(f"Found {len(conversations)} conversations.")

    print("Extracting user messages...")
    all_messages, conv_messages = extract_user_messages(conversations, user_role=args.user_role)
    print(f"Total messages extracted: {len(all_messages)}")

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    print(f"Saving all messages to {args.output}...")
    save_all_messages(all_messages, args.output)

    if args.split:
        print(f"Saving split conversations to {args.split_dir}...")
        save_split_conversations(conv_messages, args.split_dir)

    print("Done!")

if __name__ == "__main__":
    main()
