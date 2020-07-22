#!/usr/bin/python

SEQ = [3, 1, 1, 2, 0, 0, 2, 3, 3]

d_seq = {}

for i in SEQ:
    if i in d_seq:
        d_seq[i] += 1
    else:
        d_seq[i] = 1

print(d_seq)
    
