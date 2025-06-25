import argparse
import json
import os

def prepare_embeddings(input_file, output_file, min_length=50):
    with open(input_file, "r", encoding="utf-8") as f:
        raw = f.read().split("\n\n")

    docs = [msg.strip() for msg in raw if len(msg.strip()) >= min_length]

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for doc in docs:
            json.dump({"text": doc}, f, ensure_ascii=False)
            f.write("\n")

    print(f"Prepared {len(docs)} embedding documents (min_length={min_length})")

def main():
    parser = argparse.ArgumentParser(description="Prepare embeddings-ready JSONL")
    parser.add_argument("--input", required=True, help="Filtered input file")
    parser.add_argument("--output", default="output/embeddings_ready.jsonl", help="Output JSONL")
    parser.add_argument("--min_length", type=int, default=50, help="Min character length per doc")
    args = parser.parse_args()

    prepare_embeddings(args.input, args.output, args.min_length)

if __name__ == "__main__":
    main()
