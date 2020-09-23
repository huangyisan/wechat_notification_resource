#!/usr/bin/python
import json
import sys
sys.stdout.write('this is out stage')
print(json.dumps({"version": {"version": "out"}}))
