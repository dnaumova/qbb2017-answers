#!/usr/bin/env python

import sys

f=open(sys.argv[1])

lines=f.readlines()

result=[]

for line in lines:
    if line.startswith("SRR"):
        result.append(line.split('\t')[4])
    else:
        continue

f.close()

#def mean(numbers):
   # return float(sum(numbers) / len(numbers))

print float(sum(result)/len(result))

