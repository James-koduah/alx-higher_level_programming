#!/usr/bin/python3
"""Write Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write to a json file"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(json.dumps(my_obj))
