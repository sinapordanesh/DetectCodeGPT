import sys, math
from bisect import bisect_right
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, A, B = mi()
    if (A-B)%2:
        print("Borys")
    else:
        print("Alice")

if __name__ == "__main__":
    main()