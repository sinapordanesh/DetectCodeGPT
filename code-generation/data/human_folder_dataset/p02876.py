import heapq

class Heapq():
    def __init__(self,arr):
        self.que=[]
        for a in arr:
            self.que.append(-a)
        heapq.heapify(self.que)

    def pop(self):
        return -heapq.heappop(self.que)

    def push(self,a):
        heapq.heappush(self.que,-a)

    def top(self):
        return -self.que[0]

#####segfunc#####
def segfunc(x, y):
    return min(x,y)
#################

#####ide_ele#####
ide_ele = 10**15
#################

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num

        for i in range(n):
            self.tree[self.num + i] = init_val[i]

        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

import sys,random

input=sys.stdin.readline

N=int(input())
beam=[tuple(map(int,input().split())) for i in range(N)]
def solve2():
    beam.sort(key=lambda x:x[1])
    data=[min(0,beam[i][0]-beam[i][1]) for i in range(N)]
    for i in range(N-2,-1,-1):
        data[i]+=data[i+1]

    cummin=[beam[i][1] for i in range(N)]
    for i in range(N):
        if beam[i][0]-beam[i][1]>0:
            cummin[i]=10**15

    for i in range(N-2,-1,-1):
        cummin[i]=min(cummin[i],cummin[i+1])

    def cond(m):
        if m==0:
            if data[0]<=0:
                return True
            else:
                return False

        que=Heapq([])
        cnt=0
        S=0
        for i in range(N-1):
            if cnt==m:
                test=que.top()
                if beam[i][0]<test:
                    que.pop()
                    que.push(beam[i][0])
                    S+=beam[i][0]-test
            else:
                que.push(beam[i][0])
                S+=beam[i][0]
                cnt+=1
            if cnt==m:
                test=S+data[i+1]
                if test<=0:
                    return True
        return False

    start=0
    end=N
    while end-start>1:
        test=(end+start)//2
        if cond(test):
            start=test
        else:
            end=test

    if not cond(0):
        exit(print(0,1))

    m=start
    ans=[0,1]
    que=Heapq([])
    cnt=0
    S=0
    if m!=0:
        for i in range(N-1):
            if cnt==m:
                test=que.top()
                if beam[i][0]<test:
                    que.pop()
                    que.push(beam[i][0])
                    S+=beam[i][0]-test
            else:
                que.push(beam[i][0])
                S+=beam[i][0]
                cnt+=1
            if cnt==m:
                test=S+data[i+1]
                B=cummin[i+1]
                if test<=0:
                    t=abs(test)
                    if B*ans[0]<ans[1]*t:
                        ans=[t,B]

        start=[-1]*N
        end=[-1]*N
        que=[]
        trash=[]
        cnt=0
        S=0
        data1=[ide_ele]*N
        data2=[ide_ele]*N
        for i in range(N):
            if cnt==m:
                val,id=que[0]
                val=-val
                if val>beam[i][0]:
                    heapq.heappop(que)
                    heapq.heappush(trash,val)
                    end[id]=i-1
                    heapq.heappush(que,(-beam[i][0],i))
                    start[i]=i
                    S+=beam[i][0]-val
                else:
                    heapq.heappush(trash,beam[i][0])
            else:
                heapq.heappush(que,(-beam[i][0],i))
                start[i]=i
                S+=beam[i][0]
                cnt+=1
            if cnt==m:
                if i!=N-1:
                    data1[i]=S+data[i+1]
                    if trash:
                        data2[i]=S+data[i+1]+trash[0]
                    else:
                        data2[i]=S+data[i+1]
                else:
                    data1[i]=S
                    data2[i]=S+trash[0]
        for i in range(N):
            if start[i]!=-1 and end[i]==-1:
                end[i]=N-1

        Seg1=SegTree(data1,segfunc,ide_ele)
        Seg2=SegTree(data2,segfunc,ide_ele)
        for i in range(m):
            if end[i]==m-1:
                temp=Seg1.query(m,N)
                temp+=beam[i][0]-beam[i][1]
                if temp<=0:
                    temp=abs(temp)
                    B=beam[i][1]
                    if B*ans[0]<ans[1]*temp:
                        ans=[temp,B]
            else:
                L,R=m,end[i]
                temp=Seg2.query(L,R+1)-beam[i][0]
                temp+=beam[i][0]-beam[i][1]
                if temp<=0:
                    temp=abs(temp)
                    B=beam[i][1]
                    if B*ans[0]<ans[1]*temp:
                        ans=[temp,B]
                temp=Seg1.query(R+1,N)
                temp+=beam[i][0]-beam[i][1]
                if temp<=0:
                    temp=abs(temp)
                    B=beam[i][1]
                    if B*ans[0]<ans[1]*temp:
                        ans=[temp,B]
        for i in range(m,N):
            if beam[i][0]-beam[i][1]<=0:
                if start[i]==-1:
                    temp=Seg1.query(i,N)
                    temp+=beam[i][0]-beam[i][1]
                    if temp<=0:
                        temp=abs(temp)
                        B=beam[i][1]
                        if B*ans[0]<ans[1]*temp:
                            ans=[temp,B]
                else:
                    L=start[i]
                    R=end[i]
                    temp=Seg2.query(L,R+1)-beam[i][0]
                    temp+=beam[i][0]-beam[i][1]
                    if temp<=0:
                        temp=abs(temp)
                        B=beam[i][1]
                        if B*ans[0]<ans[1]*temp:
                            ans=[t,B]
                    temp=Seg1.query(R+1,N)
                    temp+=beam[i][0]-beam[i][1]
                    if temp<=0:
                        temp=abs(temp)
                        B=beam[i][1]
                        if B*ans[0]<ans[1]*temp:
                            ans=[temp,B]
            else:
                if start[i]==-1:
                    temp=Seg1.query(m-1,N)
                    temp+=beam[i][0]-beam[i][1]
                    if temp<=0:
                        temp=abs(temp)
                        B=beam[i][1]
                        if B*ans[0]<ans[1]*temp:
                            ans=[temp,B]
                else:
                    L=start[i]
                    R=end[i]
                    temp=Seg2.query(L,R+1)-beam[i][0]
                    temp+=beam[i][0]-beam[i][1]
                    if temp<=0:
                        temp=abs(temp)
                        B=beam[i][1]
                        if B*ans[0]<ans[1]*temp:
                            ans=[temp,B]
                    temp=min(Seg1.query(R+1,N),Seg1.query(m-1,L))
                    temp+=beam[i][0]-beam[i][1]
                    if temp<=0:
                        temp=abs(temp)
                        B=beam[i][1]
                        if B*ans[0]<ans[1]*temp:
                            ans=[temp,B]

    else:
        for i in range(N):
            test=data[i]
            B=cummin[i]
            if test<=0:
                t=abs(test)
                if B*ans[0]<ans[1]*t:
                    ans=[t,B]
        M=min(data)
        for i in range(N):
            if beam[i][0]-beam[i][1]>0:
                temp=M+beam[i][0]-beam[i][1]
                if temp<=0:
                    temp=abs(temp)
                    B=beam[i][1]
                    if B*ans[0]<ans[1]*temp:
                        ans=[temp,B]

    p,q=ans
    res=[q*m+p,N*q]
    from math import gcd
    g=gcd(res[0],res[1])
    return (res[0]//g,res[1]//g)

print(*solve2())