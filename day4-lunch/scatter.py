#!/usr/bin/env python

"""
okay. so. ./scatter.py <893> <915> <file name>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df1  = pd.read_csv(sys.argv[1], sep="\t")

df2  = pd.read_csv(sys.argv[2], sep="\t")

x = numpy.log(df2["FPKM"]+1)

y = numpy.log(df1["FPKM"]+1)

plt.figure()
plt.scatter(x, y, alpha=0.1, color="darkmagenta", edgecolors="none")

y_fit = numpy.polyfit(x, y, 1) 
new_x = numpy.linspace(numpy.min(x), numpy.max(x), 100)
new_y = new_x * y_fit[0] + y_fit[1]
plt.plot(new_x, new_y, "bisque")

plt.xlabel("SRR072915 FPKM")
plt.ylabel("SRR072893 FPKM")
plt.xlim(xmin=0.01)
plt.ylim(ymin=0.01)
plt.suptitle("FPKM values of SRR072893 and SRR072915")
plt.savefig(sys.argv[3] + ".png")
plt.close()



