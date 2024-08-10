import sys
from networkx.utils import UnionFind
def input(): return sys.stdin.readline().rstrip()
def main():
    h, w = map(int, input().split())
    s = [list(input()) for i in range(h)]
    uf = UnionFind()
    for i in range(h):
        for j in range(w):
            if i != h-1:
                if s[i][j] != s[i+1][j]:
                    uf.union((i*w)+j, (i*w)+j+w)
            if j != w-1:
                if s[i][j] != s[i][j+1]:
                    uf.union((i*w)+j, (i*w)+j+1)
    ans=0
    for item in uf.to_sets():
        A=0
        B=0
        for grid in item:
            i,j=divmod(grid,w)
            if s[i][j]=='.':
                A+=1
            else:
                B+=1
        ans+=A*B
    print(ans)
 
 
if __name__ == '__main__':
    main()