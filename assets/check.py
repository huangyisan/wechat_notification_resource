#!/usr/bin/python
import json
import sys
import time


def _check():
    timestamp = get_timestamp()
    return [{"version": timestamp, "stage": "check"}]


def get_timestamp():
    return str(int(time.time()))


if __name__ == "__main__":
    print(json.dumps(_check()))
