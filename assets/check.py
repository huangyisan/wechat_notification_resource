#!/usr/bin/python
import json
def _check():
  source = {"url": "mongo", "port": "27017", "db": "test", "collection": "trigger", "find": ""}
  ### LOGIC ###
  return [{"version":"1.0", "function": "in"}] # value is something Json serializable

if __name__ == "__main__":
  print(json.dumps(_check()))
