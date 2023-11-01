import json
from transformers import AutoTokenizer

# Load job listings from the JSON file
with open('norway_construction_data.json', 'r', encoding='utf-8') as file:
    job_listings = json.load(file)["content"]

# Check if there are any listings without a summary
missing_summaries = [job for job in job_listings if 'summary' not in job]

print(f"There are {len(missing_summaries)} jobs without summaries.")
for job in missing_summaries:
    print(job['uuid'])  # Print the UUID of missing jobs
# None missing for my dataset

# Extract all summaries
summaries = [job['summary'] for job in job_listings if 'summary' in job]

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-large-zh-v1.5')

# Tokenize the summaries and get the length of tokens for each summary
token_lengths = []
for idx, summary in enumerate(summaries, 1):
    token_lengths.append(len(tokenizer.tokenize(summary)))
    print(f"Tokenizing summary {idx}/{len(summaries)}...")

# Calculate the shortest, longest, and average token lengths
shortest_length = min(token_lengths)
longest_length = max(token_lengths)
average_length = sum(token_lengths) / len(token_lengths)

# Get the actual longest summary by token count
longest_summary = next(summary for summary in summaries if len(tokenizer.tokenize(summary)) == longest_length)

print(f"Shortest summary length: {shortest_length} tokens.") # 220 for my dataset
print(f"Longest summary length: {longest_length} tokens.") # 482 for my dataset



