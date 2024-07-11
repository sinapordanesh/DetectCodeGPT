#!/usr/bin/env python3
import sys
from networkx.utils import UnionFind
from operator import itemgetter
def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    city = []
    for i in range(n):
        x, y = map(int, input().split())
        city.append((x, y, i))
    city.sort(key=itemgetter(0))
    kouho = []
    for i in range(n-1):
        kouho.append((city[i+1][0]-city[i][0], city[i][2], city[i+1][2]))
    city.sort(key=itemgetter(1))
    for i in range(n-1):
        kouho.append((city[i+1][1]-city[i][1], city[i][2], city[i+1][2]))
    kouho.sort(key=itemgetter(0))
    ans = 0
    num = n
    uf = UnionFind()
    for road in kouho:
        if uf[road[1]] != uf[road[2]]:
            uf.union(road[1],road[2])
            ans+=road[0]
            num-=1
            if num==1:
                print(ans)
                break


if __name__ == '__main__':
    main()
