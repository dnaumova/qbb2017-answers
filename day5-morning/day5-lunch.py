#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], sep="\t")

roifwd = df["strand"] == "+"
roirev = df["strand"] == "-"
coi = ["chr", "start", "end", "t_name"]

df_geneplus = df[roifwd][coi]
df_geneplus["pstart"] = df_geneplus["start"] - 500
df_geneplus["pstart"][df_geneplus["pstart"]<0] = 1
df_geneplus["pend"] = df_geneplus["start"] + 500

fwds = ["chr", "pstart", "pend", "t_name"]

df_geneminus = df[roirev][coi]
df_geneminus["pstart"] = df_geneminus["end"] - 500
df_geneminus["pstart"][df_geneminus["pstart"]<0] = 1
df_geneminus["pend"] = df_geneminus["end"] + 500

revs = ["chr", "pstart", "pend", "t_name"]

both = [df_geneplus[fwds], df_geneminus[revs]]
final = pd.concat(both)

final.to_csv("blah.bed", sep="\t", header=None, index=False)