#!/usr/bin/python3
"""Take command line arguments and add them to a list"""
import sys

if __name__ == "__main__":
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    """Adds items to list form a file"""
    b = "add_item.json"
    c = []
    if len(sys.argv) == 1:
        try:
            c = load_from_json_file(b)
        except:
            save_to_json_file(c, b)

    for i in range(1, len(sys.argv)):
        c = load_from_json_file(b)
        c.append(sys.argv[i])
        save_to_json_file(c, b)

