from bisect import bisect_left, bisect_right
from math import ceil
x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()

bc = [x+y for x in b for y in c]
bc.sort()


def count_bigger_than(X):
    res = 0
    for v in a:
        res += len(bc)-bisect_right(bc,X-v-1)
    return res

  

right_bound = 3*10**10 + 1#以上の物の個数がK以下
left_bound = 0 #以上の物の個数がKより大きい

while right_bound - left_bound > 1:
    m = (right_bound + left_bound)//2
    if count_bigger_than(m)>k:
        left_bound = m
    else:
        right_bound = m


V = left_bound

ans_que = []

for v in a:
    for i in range(len(bc)-1,-1,-1):
        if v+bc[i]>=V:
            ans_que.append(v+bc[i])
        else:
            break

ans_que.sort(reverse=True)       
for i in range(k):
    print(ans_que[i])





