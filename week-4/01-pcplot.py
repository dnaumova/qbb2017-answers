#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import sys

x, y = [], []
for line in open(sys.argv[1]):
    pcs = line.rstrip("\r\n").split(" ")
    x.append(float(pcs[2]))
    y.append(float(pcs[3]))
    
plt.figure()
plt.scatter(x,y, alpha=0.5, color="springgreen")
plt.savefig("pcaplot")
plt.close()