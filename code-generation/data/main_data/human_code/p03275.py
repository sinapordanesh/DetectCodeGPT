n = int(input())
a = list(map(int,input().split()))

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)

    def sum(self, i):
        # [0, i) の要素の総和を返す
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def search(x):
    l = [1 if i >= x else -1 for i in a]
    c = [n]
    for i in range(n):
        c.append(c[-1]+l[i])

    count = 0
    bit = Bit(2*n+1)
    for i in c:
        count += bit.sum(i+1)
        bit.add(i,1)
    
    return x,count

k = (n*(n+1)/2+1)//2
le = 0
ri = max(a)+1

while ri > le + 1:
    m = (ri+le)//2
    ans,count = search(m)

    if count >= k:
        le = m
    else:
        ri = m
print(le)
