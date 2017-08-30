#!/usr/bin/env python

"""
match kmers. input probably something like: 
this file, subset file, the yak file, and kmer amount input
"""

import sys
import fasta

opensub = open(sys.argv[1])
openyak = open(sys.argv[2])

k = int(sys.argv[3])

index = {}

#adding stuff to dictionary

for ident, sequence in fasta.FASTAReader(opensub):
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in index:
            index[kmer] = [(ident,i)]
        else:
            index[kmer].append((ident,i))

#now finding matches and printing

count = 0

ident, sequence = fasta.FASTAReader(openyak).next()
#for ident, sequence in fasta.FASTAReader(openyak).next():
sequence = sequence.upper()
for i in range(0, len(sequence) - k):
    kmer = sequence[i:i+k]
    if kmer in index:
        value = index[kmer]
        for tup in value:
            count += 1
            if count > 1000:
                break
            print tup[0], "\t", tup[1], "\t", i, "\t", kmer































