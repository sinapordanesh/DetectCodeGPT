#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    S = input().replace('hi', '')
    if S == '':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
