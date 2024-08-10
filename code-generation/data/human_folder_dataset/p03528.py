K=38
#K=int(input())
N=K**2-K+1

print(N,K)
_res=[[-1 for j in range(K-1)] for i in range((K-1)**2)]
rest=[[-1 for j in range(K-1)] for i in range(K-1)]

id=K
start=0
while N>id:
    for j in range(K-1):
        _res[(K-1)*j+(start+j*((id-1)//(K-1)))%(K-1)][(id-1)//(K-1)-1]=id
    id+=1
    start=(start+1)%(K-1)

rest=[[_res[j][i] for j in range(K-1)] for i in range(K-1)]

ans=[[i for i in range(K)]]
for i in range(K-1):
    for j in range(K-1):
        tmp=[i]+_res[(K-1)*i+j]
        ans.append(tmp)
for i in range(K-1):
    tmp=[K-1]+rest[i]
    ans.append(tmp)

for i in range(N):
    ans[i]=[ans[i][j]+1 for j in range(K)]

for i in range(N):
    print(*ans[i])

def check():
    ids=[[] for i in range(N)]
    for i in range(N):
        ans[i].sort()
        if ans[i][0]<0 or ans[i][-1]>N-1:
            exit(print("WA1"))
        for j in range(1,K):
            if ans[i][j]==ans[i][j-1]:
                exit(print("WA2"))
        for j in range(K):
            ids[ans[i][j]].append(i)
    for i in range(N):
        if len(ids[i])!=K:
            exit(print("WA3"))
    p=set([])
    for i in range(N):
        for j in range(len(ids[i])):
            for k in range(j):
                a,b=ids[i][j],ids[i][k]
                if (a,b) in p:
                    print("WA4")
                    print(ans[a])
                    print(ans[b])
                    exit()

                p.add((a,b))

#check()
