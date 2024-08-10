import sys
input = sys.stdin.readline
from collections import Counter


def read():
    S = input().strip()
    return S,


def solve(S):
    D = Counter(S)
    if D["N"] != 0 and D["S"] == 0 or D["N"] == 0 and D["S"] != 0:
        return "No"
    if D["E"] != 0 and D["W"] == 0 or D["E"] == 0 and D["W"] != 0:
        return "No"
    return "Yes"


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
