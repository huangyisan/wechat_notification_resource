import json
import time

def _check():
  timestamp = get_timestamp()
  return {"version": {"version": timestamp, "stage": "in"}}

def get_timestamp():
  return str(int(time.time()))

if __name__ == "__main__":
  print(json.dumps(_check()))

