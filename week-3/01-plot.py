#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

vcol = []
afnum = []

data = open(sys.argv[1])

for line in data:
    if line.startswith ("#"):
        continue
    else:
        line = line.split("\t")
        vcfcol = line[7].split(";")
    
    af = vcfcol[3][3:]
    if "," in af:
        af = af.split(",")
        for i in af:
            afnum.append(float(i))
    else:
        afnum.append(float(af))

plt.hist(afnum)
plt.title("SacC Plot")
plt.xlabel("Allele")
plt.ylabel("Frequency")
plt.savefig("Aleelees")
plt.close


# vcffile  = open(sys.argv[1])
#
# freqs = []
# sadness = []
# sosad = []
#
# for i in data:
#     if i.startswith("#"):
#         continue
#     else:
#         fields = i.rstrip("\r\n").split("\t")
#         print "Hi"
#         sadness = fields[7].split(";")
#     #for j in fields[7]:
#         #sadness = j.split(";")
#     print "Wait what?"
#     sosad = sadness[3][3:]
#     if "," in sosad:
#         line = sadness.split(",")
#         for i in line:
#             freqs.append(float(i))
#
#             print "God damn a-a-ron"
#
#     #freqs.append(tuple[sosad])
#     else:
#         continue
#     print "Dun f'd up"
            
