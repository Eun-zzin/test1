#!/usr/bin/python


def comp1(seq:str) -> str:
    SEQ = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g')
    return SEQ.upper()

def comp2(seq:str) -> str:
    d_comp = {'A':'T','T':'A','C':'G','G':'C'}
    comp2 = ""
    for i in seq:
        comp2 += d_comp[i]
    return comp2

seq = sys.argv[1]

c1 = comp1(seq)
c2 = comp2(seq)
print(seq)
print(c1)
print(c2)


