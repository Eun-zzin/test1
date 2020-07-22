#!/usr/bin/python

import sys
import gzip # 1.gzip을 import한다


if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} {fasta.gz}")
    sys.exit()

f=sys.argv[1]
d = {}

with gzip.open(f,'rb') as handle: #2.rb = read binary
    for line in handle:
        line = line.decode("utf-8").strip()
        #4.따라서, str로 바꾸어주는 코드를 작성한다.
        if line.startswith(">"):
            continue
        for s in line:
            if s in d:
                d[s]+= 1
            else:
                d[s]=1
with open("result1.txt",'w') as handle:
    handle.write(f"A:{d['A']}\n")
    handle.write(f"G:{d['G']}\n")
    handle.write(f"C:{d['C']}\n")
    handle.write(f"T:{d['T']}\n")
