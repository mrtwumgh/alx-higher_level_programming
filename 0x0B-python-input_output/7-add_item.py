#!/usr/bin/python3
"""
A module that adds all arguments to a Python list
and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        mylist = load_from_json_file("add_item.json")
    except FileNotFoundError:
        mylist = []
    mylist.extend(sys.argv[1:])
    save_to_json_file(mylist, "add_item.json")
