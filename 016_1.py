#!/usr/bin/python

import sys
import gzip # 1.gzip을 import한다


if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} {fasta.gz}")
    sys.exit()

f=sys.argv[1]

with gzip.open(f,'rb') as handle: #2.rb = read binary
    for line in handle:
        line = line.decode("utf-8")#4.따라서, str로 바꾸어주는 코드를 작성한다.
        print(type(line.strip())) #3.type을 하면 'b'즉,binary형태라고 나온다.
        sys.exit()
