import argparse
import json
import os

def prepare_finetune(input_file, output_file, system_prompt="User:", assistant_reply=""):
    with open(input_file, "r", encoding="utf-8") as f:
        raw = f.read().split("\n\n")

    # Example: using your messages as "completions", with a placeholder prompt
    items = []
    for msg in raw:
        msg = msg.strip()
        if msg:
            item = {
                "prompt": system_prompt,
                "completion": msg
            }
            items.append(item)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for item in items:
            json.dump(item, f, ensure_ascii=False)
            f.write("\n")

    print(f"Prepared {len(items)} fine-tune items")

def main():
    parser = argparse.ArgumentParser(description="Prepare fine-tune JSONL")
    parser.add_argument("--input", required=True, help="Filtered input file")
    parser.add_argument("--output", default="output/finetune_ready.jsonl", help="Output JSONL")
    parser.add_argument("--system_prompt", default="User:", help="Prompt prefix")
    args = parser.parse_args()

    prepare_finetune(args.input, args.output, system_prompt=args.system_prompt)

if __name__ == "__main__":
    main()
