import json
from collections import defaultdict

# Load job listings from the JSON file
with open('norway_construction_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    job_listings = data["content"]

# Create a set to store unique combinations of employer name and job title
unique_combinations = set()

# Create a dictionary to group duplicate job listings by their combination
duplicates_grouped = defaultdict(list)
non_duplicate_jobs = []

# Iterate through each job listing
for job in job_listings:
    # Extract the employer name, job title, and UUID for each job listing
    employer_name = job["employer"]["name"]
    job_title = job["jobtitle"]
    job_uuid = job["uuid"]
    
    # Create a tuple of employer name and job title
    combination = (employer_name, job_title)
    
    # Check if this combination already exists in the unique_combinations set
    if combination in unique_combinations:
        duplicates_grouped[combination].append(job_uuid)
    else:
        unique_combinations.add(combination)
        non_duplicate_jobs.append(job)

# Sort and print duplicate combinations along with their UUIDs
print("Duplicate Combinations Grouped Alphabetically:")
sorted_duplicates = sorted(duplicates_grouped.items(), key=lambda x: (x[0][0], x[0][1]))  # sort by employer name and then job title

for combination, uuids in sorted_duplicates:
    employer, title = combination
    print(f"\nEmployer: {employer} - Job Title: {title}")
    for uuid in uuids:
        print(f"UUID: {uuid}")

# Print the counts for clarification
print("\nSummary:")
print(f"Original job listings: {len(job_listings)}")
print(f"Unique job listings based on employer and title: {len(non_duplicate_jobs)}")
print(f"Duplicate job listings: {len(job_listings) - len(non_duplicate_jobs)}")

# Rewrite the JSON file without duplicates
data["content"] = non_duplicate_jobs
with open('norway_construction_data_no_duplicates.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
