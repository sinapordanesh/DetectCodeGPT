X=int(input())
K=int(input())
r=list(map(int,input().split()))
Q=int(input())
p=[tuple(map(int,input().split())) for i in range(Q)]

N=Q
L=0
R=Q-1
start=0
sign="-"

# N: 処理する区間の長さ

N0 = 2**(N-1).bit_length()
data = [0]*(2*N0)
INF = 0
# 区間[l, r+1)の値をvに書き換える
# vは(t, value)という値にする (新しい値ほどtは大きくなる)
def update(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] += v

        if L & 1:
            data[L-1] += v
            L += 1
        L >>= 1; R >>= 1
# a_iの現在の値を取得
def query(k):
    k += N0-1
    s = INF
    while k >= 0:
        s += data[k]
        k = (k - 1) // 2
    return s

q=[]
for i in range(Q):
    t,a=p[i]
    p[i]=(a,t,i)

p.sort()
dic=[-1]*Q
for i in range(Q):
    a,t,id=p[i]
    update(i,i+1,a)
    dic[id]=i
    q.append((t,id,0))

for i in range(K):
    q.append((r[i],-1,r[i]-r[i-1]*(i>0)))

q.sort()
ans=[0]*Q
for val,id,c in q:
    if id==-1:
        if sign=="-":
            update(L,R+1,-c)
            while query(L+1)<0 and L<R:
                L+=1
            a=query(L)
            if a<0:
                update(L,L+1,-a)
            start=val
            sign="+"
        else:
            update(L,R+1,c)
            while query(R-1)>X and L<R:
                R-=1
            a=query(R)
            if a>X:
                update(R,R+1,X-a)
            start=val
            sign="-"
    else:
        pid,id=id,dic[id]
        if sign=="-":
            if id<L:
                res=max(query(L)-(val-start),0)
            elif id>R:
                res=max(query(R)-(val-start),0)
            else:
                res=max(query(id)-(val-start),0)
        else:
            if id<L:
                res=min(query(L)+(val-start),X)
            elif id>R:
                res=min(query(R)+(val-start),X)
            else:
                res=min(query(id)+(val-start),X)
        ans[pid]=res


for i in range(Q):
    print(ans[i])
