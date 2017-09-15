#!/usr/bin/env python

"""
making a fasta pasta
tsv to fasta
will only handle one other argument, this code is very sensitive please be kind to it
"""


import sys

fasta = open(sys.argv[1])

for pasta in fasta:
    pastas = pasta.strip("/t/n").split("/t")
    print ">" + pastas[0]

