#!/usr/bin/env python

import sys

f=open(sys.argv[1])

lines=f.readlines()

result=[]

for line in lines:
    if line.startswith("SRR"):
        add = line.split('\t'[4])
        result.append(float(add)
    else:
        continue

f.close()

stringy = ''.join(result)

floater = float(stringy)

#def mean(numbers):
   # return float(sum(numbers) / len(numbers))

print sum(result)/len(result)

