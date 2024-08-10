#!python3

from collections import deque


def LI():
    return list(map(int, input().split()))

# input
N = int(input())
A = LI()


def main():
    dq = deque()
    rev = False
    for a in A:
        if rev:
            dq.appendleft(a)
        else:
            dq.append(a)
        rev = not rev
    
    if rev:
        dq.reverse()
    
    print(*dq)


if __name__ == "__main__":
    main()
