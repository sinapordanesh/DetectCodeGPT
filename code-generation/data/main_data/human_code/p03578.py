import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())
    D = [int(x) for x in input().split()]
    M = int(input())
    T = [int(x) for x in input().split()]

    c = collections.Counter(D)

    for t in T:
        if c[t] <= 0:
            print("NO")
            return
        else:
            c[t] -= 1

    print("YES")



    

if __name__ == '__main__':
    main()

