from collections import deque
import heapq

def move(P,p):
    if p > 3:
        tmp = P[:]
        tmp[p],tmp[p-4] = tmp[p-4],tmp[p]
        tmpp = p - 4
        yield tmp,tmpp
    if p < 12:
        tmp = P[:]
        tmp[p],tmp[p+4] = tmp[p+4],tmp[p]
        tmpp = p + 4
        yield tmp,tmpp
    if p%4 > 0:
        tmp = P[:]
        tmp[p],tmp[p-1] = tmp[p-1],tmp[p]
        tmpp = p - 1
        yield tmp,tmpp
    if p%4 < 3:
        tmp = P[:]
        tmp[p],tmp[p+1] = tmp[p+1],tmp[p]
        tmpp = p + 1
        yield tmp,tmpp

def evaluate(P,Q):
    mht = 0
    for i in range(16):
        pi = P.index(i)
        qi = Q.index(i)
        pc,pr = pi//4,pi%4
        qc,qr = qi//4,qi%4
        mht += abs(pc-qc)+abs(pr-qr)
    return mht
        
A = []
B = [int(i)%16 for i in range(1,17)]
for i in range(4):
        A+=[int(i) for i in input().split()]
dp = {str(A) : (1,0),str(B) : (2,0)}
h = [(evaluate(A,B),A,0,A.index(0))]
e = [(evaluate(A,B),B,0,15)]
heapq.heapify(h)
heapq.heapify(e)
sw = False
ans = 46
while(len(h)>0 and len(e)>0):
    mht,tmp,count,p = heapq.heappop(h)
    if sw and len(h)>0:
        tmph = (mht,tmp,count,p)
        mht,tmp,count,p = heapq.heappop(h)
        heapq.heappush(h,tmph)
        sw = True
    else:
        if sw:
            sw = False
    for i,j in move(tmp,p):
        key = str(i)
        if key in dp:
            if dp[key][0] == 2:
                tmpcount = count + 1 + dp[key][1]
                if tmpcount < ans:
                    ans = tmpcount
            else:
                continue
        else:
            dp[key] = (1,count+1)
            mht = evaluate(B,i)
            if count+mht*14//13 < ans:
                heapq.heappush(h,(mht//2+count,i,count+1,j))
    _,tmp,count,p = heapq.heappop(e)
    for i,j in move(tmp,p):
        key = str(i)
        if key in dp:
            if dp[key][0] == 1:
                tmpcount = count + 1 + dp[key][1]
                if tmpcount < ans:
                    ans = tmpcount
            else:
                continue
        else:
            dp[key] = (2,count+1)
            mht = evaluate(A,i)
            if count+mht*14//13 < ans:
                heapq.heappush(e,(mht//2+count,i,count+1,j))

if str(A) == "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]":
    ans = 0
print(ans)
