class Union_find():

    def __init__(self, num):
        self.num = num
        self.par = list(range(num))
        self.rank = [0]*num

    def find(self, x):
        px = self.par[x]
        if px == x:
            return x
        else:
            rx = self.find(px)
            self.par[x] = rx
            return rx

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.par[y] = x
            else:
                self.par[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] = self.rank[y] + 1
        return self

    def same(self, x, y):
        return self.find(x) == self.find(y)

class Group_map():
    #dx, dyは原点対象となる要素を省く
    def __init__(self, H, W, dx, dy, Mat):
        self.H = H
        self.W = W
        self.dx = dx
        self.dy = dy
        self.Mat = Mat
        self.group = Union_find(H*W)

    def to_num(self, i, j):
        return i*(self.W) + j

    def grouping(self):
        for i in range(self.H):
            for j in range(self.W):
                for k in range(len(self.dx)):
                    (ni, nj) = (i + self.dx[k], j + self.dy[k])
                    if ni in range(self.H) and nj in range(self.W) and self.Mat[i][j] == self.Mat[ni][nj]:
                        self.group.union(self.to_num(i, j), self.to_num(ni, nj))
        return self

    def num_group(self, k):
        self.grouping()
        l = set()
        for i in range(self.H):
            for j in range(self.W):
                if self.Mat[i][j] == k:
                    l.add(self.group.find(self.to_num(i, j)))
        return len(l)

    def same(self, x, y):
        return self.group.same(self.to_num(x[0], x[1]), self.to_num(y[0], y[1]))

(w, h) = map(int, input().split(" "))
while w != 0 and h != 0:
    Map = []
    for i in range(h):
        Map.append(list(map(int, input().split(" "))))
    g = Group_map(h, w, [1, 1, 1, 0], [-1, 0, 1, 1], Map)
    print(g.num_group(1))
    (w, h) = map(int, input().split(" "))
    
