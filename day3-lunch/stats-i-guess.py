#!/usr/bin/env python

import sys

lens = open(sys.argv[1])

count = 0
summ = 0

for line in lens:
    stuff = line.rstrip("\r\n")
    stuffy = int(stuff)
    summ += stuffy
    count += 1
    
print "the amount of genes is %d" % (count)


print "if you want to know the sum i guess it's %d" % (summ)

averagejoe = summ/count

print "the average gene length is %d" % (averagejoe)




