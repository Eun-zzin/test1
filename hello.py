import sys

#내가한 것
base1 = ['A','G','C','T']
base2 = ['A','G','C','T']

def Mer(base1,base2,n):
    base = [] #base 내에 합친것이 쌓이도록 빈 리스트 설정함
    if n == 1: # n값이 1로 돌아오면 base2,즉 base를 base2에 담아 출력하도록!
        return base2 
    for i in base1:
        for j in base2:        
            base.append(i+j) #리스트 요소마다 더하고
    return Mer(base1,base,n-1)    
#그리고 base를 넣은 base2와 기본(A,C,G,T)가 포함된 base1을 더하여 다시 함수를 돌린다. 따라서 base1 + base가 되도록!

n = int(sys.argv[1])

print(Mer(base1,base2,n))




