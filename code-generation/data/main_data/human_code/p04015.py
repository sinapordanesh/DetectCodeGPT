def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil,pi,factorial
    from operator import itemgetter
    def I(): return int(input())
    def MI(): return map(int, input().split())
    def LI(): return list(map(int, input().split()))
    def LI2(): return [int(input()) for i in range(n)]
    def MXI(): return [[LI()]for i in range(n)]
    def SI(): return input().rstrip()
    def printns(x): print('\n'.join(x))
    def printni(x): print('\n'.join(list(map(str,x))))
    inf = 10**17
    mod = 10**9 + 7
    n,a=MI()
    lis=LI()
    for i in range(n):
        lis[i]-=a
    #print(lis)
    dp=[[0]*5001 for i in range(n+1)]
    dp[0][2500]=1
    for i in range(n):
        num=lis[i]
        for j in range(5001):
            dp[i+1][j]+=dp[i][j]
            if 0<=j+num<5001:
                dp[i+1][j+num]+=dp[i][j]
    #print(dp)
    print(dp[-1][2500]-1)
if __name__=="__main__":
    main()