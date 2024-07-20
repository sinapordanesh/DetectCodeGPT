s=list(map(int,input().split()))

oklist=[]

def keta(x):
    ketalist=[]
    for j in range(len(x)):
        ketalist.append(int(x[j]))
    return(sum(ketalist))
        
    

for i in range(s[0]+1):
    check=keta(str(i))
    if(s[1]<=check and check<=s[2]):
        oklist.append(i)     
sum_=sum(oklist)
print(sum_)