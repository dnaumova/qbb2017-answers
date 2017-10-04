#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

vcf = open(sys.argv[1])

freqs = []

for line in vcf:
    if line.startswith('#'):
        continue
    else:
        segs = line.rstrip('\r\n').split('\t')
        infreqs = segs[7].lstrip('AF=').split(',')
        for freq in infreqs:
            freqs.append(float(freq))

plt.figure()
plt.hist(freqs, bins=100, color="lightpink")
plt.xlabel( 'Allele Frequency' )
plt.savefig("alleles.png")
plt.close()