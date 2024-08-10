#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    S = input()

    win = S.count('o')
    l = len(S)
    if 15 - l >= 8 - win:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
