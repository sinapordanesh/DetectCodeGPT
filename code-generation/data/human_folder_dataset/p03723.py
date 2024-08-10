#!/usr/local/bin/python3
# https://atcoder.jp/contests/agc014/tasks/agc014_a

A, B, C = map(int, input().split())

if A == B == C and A % 2 == 0:
    print(-1)
    exit()

def check(A, B, C):
    return A%2 == 1 or B%2 == 1 or C%2 == 1

ans = 0
while check(A, B, C) == False:
    nA = (B + C) / 2
    nB = (A + C) / 2
    nC = (A + B) / 2
    A, B, C = nA, nB, nC
    ans += 1

print(ans)
