def solveequation(edge,ans,n,m):
    #edge=[[to,dire,id]...]
    x=[0]*m
    used=[False]*n

    def dfs(v):
        used[v]=True
        r=ans[v]
        for to,dire,id in edge[v]:
            if used[to]:
                continue
            y=dfs(to)
            if dire==-1:
                x[id]=y
            else:
                x[id]=-y
            r+=y
            r%=26
        return r

    for v in range(n):
        if used[v]:
            continue
        y=dfs(v)
        if y%26!=0:
            return False
    return x

alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha={i:e for e,i in enumerate(alphabetlist)}


import sys

S=input()
sys.setrecursionlimit(10**5)
n=len(S)
N=int(input())
k=n//2



if n%2==0:
    edge=[[] for i in range(k+1)]
    for i in range(N):
        l,r=map(int,input().split())
        l-=1;r-=1;
        if l>k-1:
            L=n-1-r
            R=n-1-l
            edge[L].append((R+1,-1,i))
            edge[R+1].append((L,1,i))
        elif r>k-1:
            R=n-1-r
            if R>l:
                edge[l].append((R,1,i))
                edge[R].append((l,-1,i))
            elif l>R:
                edge[l].append((R,-1,i))
                edge[R].append((l,1,i))
        else:
            edge[l].append((r+1,1,i))
            edge[r+1].append((l,-1,i))
    ans=[alpha[S[i]]-alpha[S[-i-1]] for i in range(k)]
    ans+=[0]
    for i in range(k,0,-1):
        ans[i]-=ans[i-1]
    res=solveequation(edge,ans,k+1,N)
    if res:
        print("YES")
    else:
        print("NO")
else:
    edge=[[] for i in range(k+1)]
    for i in range(N):
        l,r=map(int,input().split())
        l-=1;r-=1;
        if l>k:
            L=n-1-r
            R=n-1-l
            edge[L].append((R+1,-1,i))
            edge[R+1].append((L,1,i))
        elif l==k:
            R=k-1
            L=n-1-r
            edge[L].append((R+1,-1,i))
            edge[R+1].append((L,1,i))
        elif r>k:
            R=n-1-r
            if R>l:
                edge[l].append((R,1,i))
                edge[R].append((l,-1,i))
            elif l>R:
                edge[l].append((R,-1,i))
                edge[R].append((l,1,i))
        elif r==k:
            edge[l].append((k,1,i))
            edge[k].append((l,-1,i))
        else:
            edge[l].append((r+1,1,i))
            edge[r+1].append((l,-1,i))
    ans=[alpha[S[i]]-alpha[S[-i-1]] for i in range(k)]
    ans+=[0]
    for i in range(k,0,-1):
        ans[i]-=ans[i-1]
    res=solveequation(edge,ans,k+1,N)
    if res:
        print("YES")
    else:
        print("NO")
