from collections import deque
import sys

input=sys.stdin.readline

N=int(input())
edge=[[] for i in range(N)]
for i in range(N-1):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

parent=[-1]*N
parent[0]=0
que=deque([0])
ans=[0]
while que:
    v=que.popleft()
    for nv in edge[v]:
        if parent[nv]==-1:
            parent[nv]=v
            que.append(nv)
            ans.append(nv)

ans=ans[::-1]

def cond(n):
    dp=[-1]*N
    for v in ans:
        if v!=0:
            temp=[]
            if len(edge[v])==1:
                dp[v]=1
            else:
                for nv in edge[v]:
                    if nv!=parent[v]:
                        r=dp[nv]
                        if r==-1:
                            return False
                        temp.append(r)
                if len(temp)%2==0:
                    temp.append(0)
                temp.sort()
                start=0
                end=len(temp)-1
                while end-start>1:
                    test=(end+start)//2
                    check=True
                    s=0;t=len(temp)-1
                    while t>s:
                        if s==test:
                            s+=1
                        elif t==test:
                            t-=1
                        else:
                            if temp[s]+temp[t]>n:
                                check=False
                            s+=1
                            t-=1
                    if check:
                        end=test
                    else:
                        start=test
                check=True
                s=0;t=len(temp)-1
                while t>s:
                    if s==start:
                        s+=1
                    elif t==start:
                        t-=1
                    else:
                        if temp[s]+temp[t]>n:
                            check=False
                        s+=1
                        t-=1
                if check:
                    dp[v]=temp[start]+1
                else:
                    check=True
                    s=0;t=len(temp)-1
                    while t>s:
                        if s==end:
                            s+=1
                        elif t==end:
                            t-=1
                        else:
                            if temp[s]+temp[t]>n:
                                check=False
                            s+=1
                            t-=1
                    if check:
                        dp[v]=temp[end]+1
                    else:
                        return False
        else:
            temp=[]
            for nv in edge[v]:
                temp.append(dp[nv])
            if len(temp)%2==1:
                temp.append(0)
            temp.sort()
            k=len(temp)//2
            for i in range(k):
                test=temp[i]+temp[-i-1]
                if test>n:
                    return False
            return True

A=(len(edge[0])+1)//2
for i in range(1,N):
    A+=(len(edge[i])-1)//2

start=0
end=N-1
while end-start>1:
    test=(end+start)//2
    if cond(test):
        end=test
    else:
        start=test

print(A,end)
