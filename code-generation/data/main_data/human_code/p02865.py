#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    N = int(input())

    ans = N // 2
    if N % 2 == 0:
        ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
