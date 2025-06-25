import argparse
import os

# Simple list of "junk" phrases to skip (customize!)
JUNK_PHRASES = {"ok", "okay", "thanks", "cool", "great", "yup", "nope", "lol", "awesome", "sure", "yes", "no", "hmm"}

def is_good_message(msg, min_words=10):
    msg_lower = msg.lower().strip()
    word_count = len(msg_lower.split())
    if word_count < min_words:
        return False
    if msg_lower in JUNK_PHRASES:
        return False
    return True

def filter_messages(input_file, output_file, min_words=10):
    with open(input_file, "r", encoding="utf-8") as f:
        raw = f.read().split("\n\n")  # messages are separated by blank lines

    good_msgs = [msg.strip() for msg in raw if is_good_message(msg, min_words)]

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for msg in good_msgs:
            f.write(msg + "\n\n")

    print(f"Filtered {len(raw)} → {len(good_msgs)} messages (min_words={min_words})")
    return len(good_msgs)

def main():
    parser = argparse.ArgumentParser(description="Filter short / junk messages")
    parser.add_argument("--input", required=True, help="Input file (all_chats.txt)")
    parser.add_argument("--output", default="output/filtered_all_chats.txt", help="Filtered output file")
    parser.add_argument("--min_words", type=int, default=10, help="Minimum words per message")
    args = parser.parse_args()

    filter_messages(args.input, args.output, args.min_words)

if __name__ == "__main__":
    main()
