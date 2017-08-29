#!/usr/bin/env python

import sys

outfly = open(sys.argv[2])
readfly = outfly.readlines()

sure = open(sys.argv[1])
readsure = sure.readlines()

three = (sys.argv[3])

flyd = {}

for line in readfly:
    col = line.strip("\r\n").split()
    one = col[0]
    two = col[1]
    flyd[one] = two
    
#out = open('outfile2.txt', 'w')

ct = 0

for line in readsure:
    col = line.strip("\r\n").split("\t")
    matters = col[8]
    if matters in flyd:
        name = flyd[matters]
        col[8] = name 
    ct += 1
    if ct > 100:
        break
    print "\t".join(col)   
        #out.write('%s\t%s\n' % line, flyd)
    #out.close()