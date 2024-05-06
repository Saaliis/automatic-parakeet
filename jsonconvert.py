import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        data = list(csvreader)

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Replace 'input.csv' and 'output.json' with your CSV file name and desired JSON file name
csv_to_json('profiles1.csv', 'data.json')