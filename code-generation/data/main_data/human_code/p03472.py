import math
import sys


def input():
    return sys.stdin.readline()[:-1]


N, H = map(int, input().split())

max_a = 0
max_a_b = 0
AB = []
for _ in range(N):
    ab = list(map(int, input().split()))
    AB.append(ab)
    if max_a < ab[0]:
        max_a = ab[0]
        max_a_b = ab[1]
    elif max_a == ab[0] and max_a_b > ab[1]:
        max_a = ab[0]
        max_a_b = ab[1]

AB.sort(key=lambda x: x[1], reverse=True)

throw_sum = 0
ans = 0
for i in range(N):
    if max_a < AB[i][1]:
        throw_sum += AB[i][1]
        ans += 1
        if throw_sum >= H:
            print(ans)
            exit(0)

H -= throw_sum
ans += math.ceil(H/max_a)

print(ans)
