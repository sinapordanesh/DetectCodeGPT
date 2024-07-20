n,q=map(int,input().split())
l=list(input())
p=[]
for i in range(q):
    p.append(list(map(str,input().split())))

def solve(x):
    cs=l[x]
    ci=x
    for s,rl in p:
        if cs==s:
            if rl=='L':
                ci-=1
            else:
                ci+=1
        if ci==-1:
            return -1
        if ci==n:
            return 1
        cs=l[ci]
    return 0
        
ok=n
ng=0
while ok-ng>1:
    m=(ok+ng)//2
    s=solve(m)
    if s==-1:
        ng=m
    else:
        ok=m
ansL=ok
ok=n
ng=0
while ok-ng>1:
    m=(ok+ng)//2
    s=solve(m)
    if s==1:
        ok=m
    else:
        ng=m
ansR=ng
#print(ansR,ansL)
print(ansR-ansL+1)