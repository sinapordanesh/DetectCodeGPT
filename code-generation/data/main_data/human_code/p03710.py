from math import gcd
import random,time

def gcdcount(n,m):
    x,y=min(n,m),max(n,m)
    if x==0:
        return 0
    else:
        return 1+gcdcount(x,y%x)

fibo=[0,1,2]
for i in range(100):
    fibo.append(fibo[-1]+fibo[-2])

gcdfibo=[[],[(1,2),(1,3)]]

for i in range(2,101):
    temp=[]
    for a,b in gcdfibo[-1]:
        temp.append((b,a+b))
    a,b=fibo[i],fibo[i+2]
    temp.append((a,b))
    temp.sort()
    gcdfibo.append(temp)

def solve(x,y):
    if x>y:
        x,y=y,x
    mod=10**9+7
    if x==1:
        return  (1,y%mod)
    if (x,y)==(2,2):
        return (1,3)
    id=1
    t=-1
    while True:
        if fibo[id+1]<=x and fibo[id+2]<=y:
            id+=1
        else:
            if fibo[id+1]>x:
                if fibo[id+2]>y:
                    t=0
                else:
                    t=1
            else:
                t=2
            break

    #print(t)
    if t==0:
        res=0
        for a,b in gcdfibo[id]:
            if a<=x and b<=y:
                res+=1
        return (id,res)
    elif t==1:
        res=0
        for a,b in gcdfibo[id]:
            if a<=x and (a,b)!=(fibo[id],fibo[id+2]) and b<=y:
                res+=(y-b)//a+1
                res%=mod
        return (id,res)
    else:
        res=0
        for a,b in gcdfibo[id+1]:
            u,v=b-a,a
            if u<=x and v<=y:
                res+=1
                res%=mod
            if u<=y and v<=x:
                res+=1
                res%=mod
        return (id,res)

mod=10**9+7
Q=int(input())
start=time.time()
for _ in range(Q):
    x,y=map(int,input().split())
    id,res=solve(x,y)
    if (x,y)==(2,2):
        res+=1
    print(id,res)

#print(time.time()-start)