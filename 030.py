#!/usr/bin/python

import sys

def findindex(seq):
    for i in range(len(seq)):
        if seq[i:i+2] == 'TT':
            print(i)
        else:
            continue

seq1 = sys.argv[1]
result = findindex(seq1)


