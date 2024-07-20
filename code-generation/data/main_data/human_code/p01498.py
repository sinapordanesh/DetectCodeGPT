import sys

class UnionFind:
    def __init__(self,sz):
        self.__ranks = [1] * sz
        self.__parents = [ i for i in range(sz) ]
    def find_parent(self, x):
        if x == self.__parents[x]:
            return x
        else:
            self.__parents[x] = self.find_parent(self.__parents[x])
            return self.__parents[x]
    def same(self, x, y):
        return self.find_parent(x) == self.find_parent(y)
    def unite(self, x, y):
        px = self.find_parent(x)
        py = self.find_parent(y)
        if px == py:
            return
        if self.__ranks[px] > self.__ranks[py]:
            self.__parents[py] = px
        else:
            self.__parents[px] = py
            if self.__ranks[px] == self.__ranks[py]:
                self.__ranks[py] += 1

def main():
    n,w,h = map(int, input().split())

    uf = UnionFind(n)
    xd = {}
    yd = {}
    is_edges_slime = False
    for i in range(n):
        x,y = map(int, sys.stdin.readline().split())

        if x == 1 or x == w:
            is_edges_slime = True
        if y == 1 or y == h:
            is_edges_slime = True

        if x in xd:
            uf.unite(xd[x], i)
        else:
            xd[x] = i
        
        if y in yd:
            uf.unite(yd[y], i)
        else:
            yd[y] = i

    root = set()
    for i in range(n):
        root.add( uf.find_parent(i) )

    if len(root) == 1:
        print(n - 1)
    else:
        ans = n - len(root) # ????´?????????¨??????
        ans += len(root) - (1 if is_edges_slime else 0) # ???????????????
        ans += len(root) - 1 # ????????°???????????????
        print(ans)

if __name__ == '__main__':
    main()