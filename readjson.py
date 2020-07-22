#!/usr/bin/python

# csv, tsv 파일 파이썬으로 읽고 각 줄마다 id, sequence, species로 분류하기.
import sys
import json

def read_txt(filename :str) -> str:
    ret = ""
    with open(filename,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret

def read_csv(filename:str) -> list: 
    #csv파일 읽고, ','값으로 구분하여 딕셔너리형태로 만들기
    ret = []
    with open(filename, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def read_tsv(filename:str) -> list:
#tsv파일을 읽어서 \t기준으로 구분해주기
    ret = []
    with open(filename, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def to_json(l:list,file_name:str) -> None: #json은 list형태만을 받는다.
    with open(file_name,'w') as handle:
        json.dump(l,handle,indent=4)

def read_json(file_name: str) -> list:
    with open(file_name,'r') as handle:
        l = json.load(handle) #
    return l

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("#usage : python {sys.argv[0]} {txt}")
        sys.exit()

    filename = sys.argv[1]
    ret = read_tsv(filename) #tsv를 부른다음에
    to_json(ret,"result.json") #json 파일로 변환한다.

