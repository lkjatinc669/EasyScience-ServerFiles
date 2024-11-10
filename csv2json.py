import csv
import json

def convertToJson(csv_file_path, json_file_path):
    # Initialize list to store data
    data = []

    # Read CSV file
    with open(csv_file_path, mode='r', newline='', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Write to JSON file
    with open(json_file_path, mode='w', encoding='utf-8-sig') as json_file:
        json.dump(data, json_file, indent=4)


convertToJson("chapter.csv", "chapter.json")
convertToJson("paper.csv", "paper.json")