# FASTA : count_base() 
# 메소드 : file_name -> str
#        : count -> dict
#         : length : int

import sys

class FASTA:
    def __init__(self,file_name:str):
        self.file_name = file_name
        self.count = {} #count 값
        self.length = 0 #length 값

    def count_base(self):
        with open(self.file_name, 'r') as handle:
            for line in handle:
                if line.startswith(">"): #>로 시작하는 것은 제외한다.
                    continue
                line = line.strip() # '\n'을 삭제해준다.
                for s in line:
                    if s in self.count:
                        self.count[s] += 1
                    else:
                        self.count[s] = 1
       
    def get_length(self): #길이를 구한다.
        length = 0
        for k,v in self.count.items(): 
        #count가 dict형태이기 때문에 key,val 두개값을 주어야한다.
            self.length += v

#    def __len__(self):
#        self.get_length()
#        return self.length

if __name__=="__main__": 
# "__name__" : import를 하면 if절 내의 명령을 제외하고 실행시켜준다. 
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} {fasta}")
        sys.exit()
    file_name = sys.argv[1]
    t = FASTA(file_name) 
    t.count_base() #count_base를 먼저 실행해야
    print(t.count)
    t.get_length() #length를 count할 수 있다. (count 변수가 필요하기 때문)
    print(t.length)
