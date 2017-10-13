#!/usr/bin/env python

import sys
import itertools
import fasta

nukes = open(sys.argv[1])
protes = open(sys.argv[2])

nukeprot = open("nukeprot.fa","w")

for (nident, nseq), (pident, pseq) in itertools.izip(fasta.FASTAReader(nukes), fasta.FASTAReader(protes)):
    nukeprot.write(nident + "\n")
    for aa in pseq:
        if aa == "-":
            nukeprot.write("---")
        else:
            nukeprot.write(nseq[:3])
            nseq = nseq[3:]
        nukeprot.write("/n")