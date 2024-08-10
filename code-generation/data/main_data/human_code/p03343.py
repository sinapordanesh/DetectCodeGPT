def main(n,k,q,x):
    ret=float('inf')
    for xi in x:
        c=[]
        tmp=[]
        for y in x:
            if y<xi:
                if len(tmp)>=k:
                    tmp.sort()
                    for j in range(len(tmp)-k+1):
                        c.append(tmp[j])
                tmp=[]
            else:
                tmp.append(y)
        if len(tmp)>=k:
            tmp.sort()
            for j in range(len(tmp)-k+1):
                c.append(tmp[j])
        if len(c)>=q:
            c.sort()
            ret=min(ret,c[q-1]-xi)
    return ret

#n=int(input())
#a=list(input())
#a=list(map(int,input().split()))
#b=list(map(int,input().split()))
#ab=[list(map(int,input().split())) for _ in range(n)]
n,k,q=map(int,input().split())
x=list(map(int,input().split()))
print(main(n,k,q,x))
