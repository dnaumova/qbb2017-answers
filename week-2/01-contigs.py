#!/usr/bin/env python

"""
computing number of contigs, min/max/average contig length, N50.
i guess you do it for the velvet and the spades files separately?
./01-contigs.py <velvet> <spades>
"""

import sys
import fasta
import operator

velvet = open(sys.argv[1])
spades= open(sys.argv[2])

total_l = 0
vcontigs = []
for name, seq in fasta.FASTAReader(velvet):
    seq = seq.upper()
    sub = [name, seq, len(seq)]
    total_l += len(seq)
    vcontigs.append(sub)
#print vcontigs
vcontigs = sorted(vcontigs, key=operator.itemgetter(2), reverse=True)
#contigs.sort()

print "velvet: num contigs = %d" % (len(vcontigs))

print "velvet: min contig length = %d" % (vcontigs[0][2])
#or max(contigs), min(contigs)
print "velvet: max contig length = %d" % (vcontigs[-1][2])

average = float(total_l)/float(len(vcontigs))

print "velvet: average contig length = %f" % (average)

ldiv = float(total_l) / 2.0

tot = 0
for each in vcontigs:
    tot += each[2]
    if tot >= ldiv:
        n50 = each
        break

print "velvet: n50 = %s" % (n50[2])

#now for spades

total_l = 0
scontigs = []
for name, seq in fasta.FASTAReader(spades):
    seq = seq.upper()
    sub = [name, seq, len(seq)]
    total_l += len(seq)
    scontigs.append(sub)
#print scontigs
scontigs = sorted(scontigs, key=operator.itemgetter(2), reverse=True)
#contigs.sort()

print "spades: num contigs = %d" % (len(scontigs))

print "spades: min contig length = %d" % (scontigs[0][2])
#or max(contigs), min(contigs)
print "spades: max contig length = %d" % (scontigs[-1][2])

average = float(total_l)/float(len(scontigs))

print "spades: average contig length = %f" % (average)

ldiv = float(total_l) / 2.0

tot = 0
for each in scontigs:
    tot += each[2]
    if tot >= ldiv:
        n50 = each
        break

print "spades: n50 = %s" % (n50[2])

    











