import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import math

# 反転で同心円に帰着する

T = int(input())
query = [[int(x) for x in input().split()] for _ in range(T)]

def solve_2_eq(a,b,c):
    return (-b + (b*b-4*a*c)**.5) / (2*a)

def F(r,R,d):
    # 複比
    ratio = ((d+r+R)*(d-R-r)) / (4*r*R)
    
    R = solve_2_eq(1,-2-4*ratio, 1)
    # 内側の円が1, 外側の円が半径Rであるような同心円に帰着
    r = (R-1)/2
    theta = math.asin(r/(1+r))
    return int(math.pi // theta)

answer = []
for data in query:
    d = ((data[3]-data[0])**2 + (data[4]-data[1])**2) ** .5
    answer.append(str(F(data[2],data[5],d)))

print('\n'.join(answer))