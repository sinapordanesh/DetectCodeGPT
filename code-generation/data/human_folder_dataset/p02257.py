
import math

##素数判定を行う関数
def prime(p):
    if p==2 or p==3:
        return True
    else:
        i = int(math.sqrt(p))
        while i>=2:
            if p%i==0:
                return False
                break
            i-=1
        return True
                
            

N = int(input())
count = 0

for i in range(N):
    a = int(input())
    if prime(a)==True:
        count+=1
        
print(count)
