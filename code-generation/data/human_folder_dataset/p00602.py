import sys
sys.setrecursionlimit(10000000)
MOD = 1001
INF = 10 ** 15

class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x): #根を見つける、繋ぎ直す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def unite(self,x,y): #x,yの含むグループを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x,y = y,x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def same(self,x,y):#xとyが同じグループにいるか判定
        return self.find(x) == self.find(y)
    
    def members(self,x):#xと同じグループのメンバーを列挙
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def size(self,x):#xが属するグループのメンバーの数
        return -self.parents[self.find(x)]
    
    def roots(self):#ufの根を列挙
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):#グループの数を数える
        return len(self.roots())

def solve(V,d,fib):
    uf  = UnionFind(V)
    for i in range(V):
        for j in range(i + 1,V):
            if abs(fib[i] - fib[j]) < d:
                uf.unite(i,j)
    ans = uf.group_count()
    print(ans)

def main():
    fib = [0] * 1005
    fib[0] = 2; fib[1] = 3
    for i in range(2,1005):
        fib[i] = fib[i - 1] + fib[i - 2]
        fib[i] %= MOD
    
    while True:
        try:
            V,d = map(int,input().split())
            solve(V,d,fib)
        except:
            return
if __name__ == '__main__':
    main()
