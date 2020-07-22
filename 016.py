#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print(f"#usage : python {sys.argv[0]} [fasta]")
    sys.exit()

f = sys.argv[1]
d = {}

with open(f,'r') as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        for s in line.strip(): #한글자씩 넘어온다.
            if s in d:
                d[s] += 1 #안에 이미 있는 글자면 하나 더하고,
            else:
                d[s] = 1 # 없다면 1을 기본값을 둔다.

print(d)

total = 0
for k,v in d.items():
    total += v

with open("write_sample.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n") #"와 '를 구분하여 써야한다. 안그러면 앞/뒤 나눠짐
    handle.write(f"C: {d['C']}\n") #"와 '를 구분하여 써야한다. 안그러면 앞/뒤 나눠짐
    handle.write(f"G: {d['G']}\n") #"와 '를 구분하여 써야한다. 안그러면 앞/뒤 나눠짐
    handle.write(f"T: {d['T']}\n") #"와 '를 구분하여 써야한다. 안그러면 앞/뒤 나눠짐
    


