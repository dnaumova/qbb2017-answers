#!/usr/bin/env python

import sys

samfile = open(sys.argv[1])

count = 0

for line in samfile:
    if "NM:i:" in line:
        count = count + 1
    else: 
        continue

print count
    
