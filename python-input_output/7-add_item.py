#!/usr/bin/python3
"""
module to import arguments json

"""
from sys import argv as av
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    P_list = load_from_json_file('add_item.json')
except Exception:
    P_list = []
for i in av[1:]:
    P_list.append(i)

save_to_json_file(P_list, 'add_item.json')
