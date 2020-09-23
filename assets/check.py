#!/usr/bin/python
import json
import sys
def _check():
  source = {"url": "mongo", "port": "27017", "db": "test", "collection": "trigger", "find": ""}
  ### LOGIC ###
  return [{"version":"1.0", "function": "check"}] # value is something Json serializable

if __name__ == "__main__":
  sys.stdout.write('this is check stage')
  print(json.dumps(_check()))
