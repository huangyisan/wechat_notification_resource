#!/usr/bin/python
import json
import sys
def _check(args):
  source = {"url": "mongo", "port": "27017", "db": "test", "collection": "trigger", "find": ""}
  ### LOGIC ###
  print(json.load(args))
  return [{"version":"2.0", "function": 11}] # value is something Json serializable

if __name__ == "__main__":
  sys.stdout.write('check') 
  print(json.dumps(_check(sys.stdin)))
