#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

fpk = pd.read_csv(sys.argv[1], sep="\t")
#fpk = fpk.sort_values(by="t_name")
df_fpk = fpk["FPKM"]

listy = []

for blah in sys.argv[2:]:
    df = pd.read_csv(blah, sep="\t", header=None, names = ["name", "size", "covered", "sum", "mean0", "mean"])
    #df = df.sort_values(by="name")
    dfblah = df.iloc[:,5]
    model = sm.OLS(dfblah,df_fpk)
    results = model.fit()
    print results.summary()   