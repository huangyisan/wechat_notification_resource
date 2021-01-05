#!/usr/bin/python
import json


def _check():
    return {"version": {"version": "static", "stage": "in"}}

if __name__ == "__main__":
    print(json.dumps(_check()))
