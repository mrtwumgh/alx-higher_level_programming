#!/usr/bin/python3
"""
A script that adds all arguments to a python list,
and then saves them to a file
"""
import json
import sys


if __name__ == "__main__":
    save_to_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        mylist = load_from_file("add_item.json")
    except FileNotFoundError:
        mylist = []

    mylist.extend(sys.argv[1:])
    save_to_file(mylist, "add_item.json")
