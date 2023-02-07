#!/usr/bin/python3
import json

"""To a JSON representation"""


def to_json_string(my_obj):
    """to_json_string converts an obj into JSON

    Return: a JSON representation of an object
    """
    return (json.dumps(my_obj))
