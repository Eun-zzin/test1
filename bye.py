import json

f = "read_sample.csv"

with open(f,'r') as fr:
    for line in fr:
        print(line.strip().split(","))
