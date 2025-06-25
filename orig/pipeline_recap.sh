# Step 1: extract from conversations.json
python3 chat_parser.py --input conversations.json

# Step 2: filter
python3 quality_filter.py --input output/all_chats.txt

# Step 3: embeddings
python3 prep_for_embeddings.py --input output/filtered_all_chats.txt

# Step 4: fine-tune
python3 prep_for_finetune.py --input output/filtered_all_chats.txt
