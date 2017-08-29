#!/usr/bin/env python

import sys

f=open(sys.argv[1])

lines=f.readlines()

result=[]

for line in lines:
    if "AS:" not in line:
        continue
    if len(result) > 10:
        break
    else:
        result.append(line.split('\t')[2])

f.close()

print result [0:10]

