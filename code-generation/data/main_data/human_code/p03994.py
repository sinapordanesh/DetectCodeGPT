import sys, math
from itertools import accumulate
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
    s, K = input(), ii()
    l = list(map(lambda c: (ord('z')-ord(c)+1)%26, s))

    acc = 0
    t = ['']*len(s)
    for i in range(len(s)):
        if acc + l[i] <= K:
            acc += l[i]
            t[i] = 'a'
        else:
            t[i] = s[i]

    if i == len(s)-1 and K-acc > 0:
        t[i] = chr((ord(t[i])-ord('a')+K-acc)%26+ord('a'))

    print(''.join(t))

if __name__ == "__main__":
    main()