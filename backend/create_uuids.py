import json
import uuid

# Load the JSON data from the file
with open('norway_construction_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Overwrite the UUID for each item in the content list
for item in data['content']:
    item['uuid'] = str(uuid.uuid4())

# Write the modified data back to the file
with open('norway_construction_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

print("UUIDs have been successfully created!")
