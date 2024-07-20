def f(m,a,b,p):
    for i in range(m,0,-1):
        for j in range(2,-~int(i**.5)):
            if p[j] and i%j==0:
                q=i//j
                if a*q<=b*j and j<=q and p[q]:print(j,q);return
n=100000
p=[0]*2+[1]*(n-2)
for i in range(2,-~int(n**.5)):
    if p[i]:
        for j in range(i*i,n,i):
            p[j]=0
while 1:
    m,a,b=map(int,input().split())
    if m==0:break
    f(m,a,b,p)