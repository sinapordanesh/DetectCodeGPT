#!/usr/bin/env python3
def right_triangle(edge):
    # a < b < c
    return (edge[0] ** 2 + edge[1] ** 2 == edge[2] ** 2)

n = int(input())
for i in range(n):
    edge = sorted([int(x) for x in input().split()])
    if right_triangle(edge):
        print("YES")
    else:
        print("NO")