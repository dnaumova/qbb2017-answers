#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import fasta

data  = open(sys.argv[1])

count = 0
plt.figure()
for i in data:
    if "zstart1" in i:
        continue
    else:
        fields = i.rstrip("\r\n").split("\t")
        #print fields
        plt.plot([count,count+(float(fields[1])-float(fields[0]))], [float(fields[0]),float(fields[1])])
        count += float(fields[1])-float(fields[0])

plt.xlabel("Contigs")
plt.ylabel("Position")
plt.ylim((0,100000))
plt.xlim((0,100000))
#plt.savefig("NP Lastz")
#plt.savefig("Spades Lastz")
#plt.savefig("Velvet Lastz")
plt.savefig("Spades Better")
#plt.savefig("Velvet Better")

