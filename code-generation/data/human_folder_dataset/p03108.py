class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.components = [1]*n  # 各連結成分の大きさ

    def root(self, x):
        if self.p[x] != x:
            stack = [x]
            while True:
                top = stack[-1]
                if self.p[top] == top:
                    break
                else:
                    stack.append(self.p[top])
            for v in stack:
                self.p[v] = top
        return self.p[x]
    
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            self.p[x] = y
            size_x , size_y = self.components[x], self.components[y]
            self.components[x] = size_x + size_y
            self.components[y] = size_x + size_y

            return size_x * size_y

        return 0


    
    def same(self, x,y):
        return (self.root(x) == self.root(y))

N, M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]
AB.reverse()

UF = UnionFind(N)

ans = [N*(N-1)//2]
for a, b in AB:
    a, b = a-1, b-1
    ans.append(ans[-1] - UF.unite(a,b))

ans.reverse()
for a in ans[1:]: 
    print(a)
   