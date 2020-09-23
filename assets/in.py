#!/usr/bin/python
import json
import sys
import time

def get_timestamp():
    return str(int(time.time()))

def _check():
    timestamp = get_timestamp()
    return {"version": {"version": get_timestamp()}}

if __name__ == "__main__":
    print(json.dumps(_check()))
