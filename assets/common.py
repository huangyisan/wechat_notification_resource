
from __future__ import print_function
import sys
import os


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


os.system("echo 1 > 1.f")
with open('1.f', 'r') as f:
    line = f.read()
print(line)