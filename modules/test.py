import json

with open('./prayers.json', 'r', encoding='utf-8') as json_file:
    prayers = json.load(json_file)
    print(prayers)
