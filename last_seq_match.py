#!/usr/bin/env python3
# Go line by line of file1 and try to match with file2
# returns the last match.
# obs: file1 and file2 are sequencial

import sys
import re

last_match = None


if len(sys.argv) != 3:
    print('usage: %s <file1> <file2>' % sys.argv[0])
    print(
        'It will return the last line of file1' +
        'that matches some line in file2')
    exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

retryCount = 10

with open(file2) as f:
    src = f.read()
    x = 0
    for line in open(file1):
        line = line.strip()
        if(line in src):
            last_match = line
            x = 0
        else:
            if x >= retryCount:
                break
            else:
                x += 1

print(last_match if last_match else 'No matches')
