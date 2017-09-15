#!/usr/bin/env python

import sys
import fasta
import itertools
import numpy as np
import matplotlib.pyplot as plt

nukes = open(sys.argv[1])

therealmvp = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
justseq = []
for name, seq in fasta.FASTAReader(nukes):
    justseq.append(seq)

dN = []
dS = []
for something in range(0,4871):
    dN.append(0)
    dS.append(0)
    
watseq = justseq[:1]
disseq = justseq[:1]

watcodon = []
discodon = []
dracula = 0
while dracula < 14614:
    wat = watseq[0][dracula:dracula+3]
    dis = disseq[0][dracula:dracula+3]
    watcodon.append(wat)
    discodon.append(dis)
    dracula += 3

for ugh in range(len(disseq)):
    chocula = 0
    codchocula = 0
    while chocula < 14614:
        wat = watseq[ugh][chocula:chocula+3]
        dis = disseq[ugh][chocula:chocula+3]
        if "-" in disseq[ugh][chocula:chocula+3]:
            codchocula += 1
            chocula += 3
        elif "-" in watseq[0][chocula:chocula+3]:
            codchocula += 1
            chocula += 3
            #print "u missed something"
        elif wat not in therealmvp:
            chocula += 3
        elif watseq[ugh][chocula:chocula+3] == disseq[0][chocula:chocula+3]:
            codchocula += 1
            chocula += 3
            #print "ugh"
        elif therealmvp[dis] != therealmvp[wat]:
            dN[codchocula] = dN[codchocula] + 1
            codchodula += 1
            chocula += 3
            #print "just give up"
        elif therealmvp[dis] == therealmvp[wat]:
            dS[codchocula] = dS[codchocula] + 1
            codchocula += 1
            chocula += 3
        else:
            print "no more errors pls"
        
changes = [int(n) - int(s) for n,s in zip (dN, dS)]

print len(dN)
print len(dS)
print changes

plt.figure()
plt.plot(changes)
plt.xlabel("Gene Location")
plt.ylabel("dN-dS")
plt.savefig("w1-ztest" + ".png")
plt.close()
