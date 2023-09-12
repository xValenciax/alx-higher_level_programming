#!/usr/bin/python3

"""
a script that adds command line arguments
to a python list and then save it to a file
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_file = 'add_item.json'
args = []

for arg in sys.argv:
    args.append(arg)

args.pop(0)

list_from_json = []

try:
    list_from_json = load_from_json_file(json_file)
except FileNotFoundError as e:
    with open(json_file, 'w+', encoding='UTF-8') as f:
        json.dump(list_from_json, f)

list_to_json = list_from_json + args
save_to_json_file(list_to_json, json_file)
