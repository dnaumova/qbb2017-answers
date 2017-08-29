#!/usr/bin/env python

import sys

#Opening file with open
##f = open("/Users/cmdb/data/genomes/BDGP6.fa")

#open file using input, read first line
if len(sys.argv) > 1:
    f = open(sys.argv[1])
    first_line = f.readline()
else:
    first_line = sys.stdin.readline()

print first_line







































