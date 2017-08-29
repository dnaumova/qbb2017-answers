#!/usr/bin/env python

import sys

fly=open(sys.argv[1])

readfly=fly.readlines()

dromes={}

ct = 0

for item in readfly:
    if "DROME" in item:
        column = item.rstrip("\r\n").split()
        if len(column)!=4:
            continue        
        ac = column[2]
        flybase = column[3]
        dromes[str(flybase)] = str(ac)
        ct += 1
        if ct > 100:
            break
    else:
        continue

out = open('outfile.txt', 'w')
for key, value in dromes.iteritems():
    out.write('%s\t%s\n' % (key,value))
out.close()






















