import sys
from networkx.utils import UnionFind
def input(): return sys.stdin.readline().rstrip()


def main():
    n,m=map(int, input().split())
    lang=[[] for i in range(m+1)]
    for i in range(1,n+1):
        for talk in list(map(int, input().split()))[1:]:
            lang[talk].append(i)
    uf = UnionFind()
    for langs in lang:
        if len(langs) >=1:
            uf.union(*langs)
    print('YES' if len(list(uf.to_sets()))==1 else 'NO')
    




if __name__ == '__main__':
    main()
