# FASTA : count_base() 
# 메소드 : file_name -> str
#        : count -> dict
#         : length : int

import sys

class FASTA: #FASTA파일 class
    def __init__(self,file_name:str):
        self.file_name = file_name
        self.count = {} #count 값
        self.length = 0 #length 값

    def count_base(self):
     with open(self.file_name, 'r') as handle:
        for line in handle:
            if line.startswith(">"): #>로 시작하는 것은 제외한다.
                continue
            line = line.strip()
            for s in line:
                if s in self.count:
                    self.count[s] += 1
                else:
                    self.count[s] = 1
       
    def get_length(self): #길이를 구한다.
        length = 0
        for k,v in self.count.items():
            self.length += v

    def __len__(self):
        self.get_length()
        return self.length

class FASTQ:
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.read_num = 0
        self.base = {}

    def count_read_num(self):
        cnt = 0
        with open(self.file_name,'r') as handle:
            for line in handle:
                if cnt % 4 ==0: #가장 첫줄(header)
                    header = line.strip()
                    self.read_num +=1
                elif cnt %4 == 1: #두번째 줄(seq)
                    seq = line.strip()
                    for s in seq:
                        if s in self.base:
                            self.base[s] +=1
                        else:
                            self.base[s] =1
                elif cnt %4 ==3: #세번째 줄(quality)
                    qual = line.strip()
                cnt+=1

    def count_base_num(self):
        cnt = 0
        cnt += self.base.values()
        return cnt

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} {fasta}")
        sys.exit()
    file_name = sys.argv[1]
#    t = FASTA(file_name) 
#    t.count_base() #count_base를 먼저 실행해야
#    print(t.count)
#    t.get_length() #length를 count할 수 있다. (count 변수가 필요하기 때문)
#    print(t.length)

    q = FASTQ(file_name)
    q.count_read_num()
    print(q.read_num)
    print(q.base)
