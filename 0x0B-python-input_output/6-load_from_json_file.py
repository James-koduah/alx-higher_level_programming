#!/usr/bin/python3
"""load form json file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, encoding='utf-8') as a_file:
        b = json.loads(a_file.read())
