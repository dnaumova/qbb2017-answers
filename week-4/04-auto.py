#!/usr/bin/env python

import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math

new_list = ["plink.Cadmium_Chloride.assoc.linear","plink.Mannose.assoc.linear","plink.Caffeine.assoc.linear","plink.Menadione.assoc.linear","plink.Calcium_Chloride.assoc.linear","plink.Neomycin.assoc.linear","plink.Cisplatin.assoc.linear","plink.Paraquat.assoc.linear","plink.Cobalt_Chloride.assoc.linear","plink.Raffinose.assoc.linear","plink.Congo_red.assoc.linear","plink.SDS.assoc.linear","plink.Copper.assoc.linear","plink.Sorbitol.assoc.linear","plink.Cycloheximide.assoc.linear","plink.Trehalose.assoc.linear","plink.Diamide.assoc.linear","plink.Tunicamycin.assoc.linear","plink.E6_Berbamine.assoc.linear","plink.Xylose.assoc.linear","plink.Ethanol.assoc.linear","plink.YNB.assoc.linear","plink.Formamide.assoc.linear","plink.YNB:ph3.assoc.linear","plink.Galactose.assoc.linear","plink.YNB:ph8.assoc.linear","plink.Hydrogen_Peroxide.assoc.linear","plink.YPD.assoc.linear","plink.Hydroquinone.assoc.linear","plink.YPD:15C.assoc.linear","plink.Hydroxyurea.assoc.linear","plink.YPD:37C.assoc.linear","plink.Indoleacetic_Acid.assoc.linear","plink.YPD:4C.assoc.linear","plink.Lactate.assoc.linear","plink.Zeocin.assoc.linear","plink.Lactose.assoc.linear","plink.x4-Hydroxybenzaldehyde.assoc.linear","plink.Lithium_Chloride.assoc.linear","plink.x4NQO.assoc.linear","plink.Magnesium_Chloride.assoc.linear","plink.x5-Fluorocytosine.assoc.linear","plink.Magnesium_Sulfate.assoc.linear","plink.x5-Fluorouracil.assoc.linear","plink.Maltose.assoc.linear","plink.x6-Azauracil.assoc.linear"]

for i in range(len(new_list)):
    os.system("./03-manhat.py " + str(new_list[i]) + " " + str(new_list[i][6:9]))