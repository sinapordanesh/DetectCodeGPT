class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def calc_group_num(self):
        N = len(self._parent)
        ans = 0
        for i in range(N):
            if self.find_root(i) == i:
                ans += 1
        return ans

mod = 10**9+7 #出力の制限
N = 2*10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

import sys,bisect

input=sys.stdin.buffer.readline

N,X,Y=map(int,input().split())
cball=[[] for i in range(N)]
ball=[]
color=[-1]*N
for i in range(N):
    c,w=map(int,input().split())
    ball.append((w,c-1,i))
    cball[c-1].append((w,i))
    color[i]=c-1

for i in range(N):
    cball[i].sort()
ball.sort()

if N==1:
    print(1)
    exit()

cmin=[10**20 for i in range(N)]
for i in range(N):
    if cball[i]:
        cmin[i]=min(cball[i][j][0] for j in range(len(cball[i])))

_cmine1=[cmin[i] for i in range(N)]
_cmine2=[cmin[i] for i in range(N)]
for i in range(1,N):
    _cmine1[i]=min(_cmine1[i],_cmine1[i-1])
for i in range(N-2,-1,-1):
    _cmine2[i]=min(_cmine2[i],_cmine2[i+1])
cmine=[0]*N
cmine[0]=_cmine2[1]
cmine[-1]=_cmine1[N-2]
for i in range(1,N-1):
    cmine[i]=min(_cmine1[i-1],_cmine2[i+1])

M=min(ball)
special=-1
for i in range(N):
    if cmine[i]!=M[0]:
        special=i

uf=UnionFindVerSize(N)
for i in range(N):
    if i!=special:
        for j in range(len(cball[i])):
            if M[0]+cball[i][j][0]<=Y:
                uf.unite(cball[i][j][1],M[2])
            if j!=0 and cball[i][j][0]+cball[i][0][0]<=X:
                uf.unite(cball[i][j][1],cball[i][0][1])
    else:
        for j in range(len(cball[special])):
            if cmine[special]+cball[special][j][0]<=Y:
                uf.unite(cball[special][j][1],M[2])
            if M[0]+cball[special][j][0]<=X:
                uf.unite(cball[special][j][1],M[2])

connect={}
for i in range(N):
    root=uf.find_root(i)
    if root not in connect:
        connect[root]=[]
    connect[root].append(i)

ans=1
for root in connect:
    cc={}
    for i in connect[root]:
        if color[i] not in cc:
            cc[color[i]]=0
        cc[color[i]]+=1
    size=len(connect[root])
    for C in cc:
        ans*=g2[cc[C]]
        ans%=mod
    ans*=g1[size]
    ans%=mod

print(ans)