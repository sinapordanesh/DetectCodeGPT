import math
n = int(input())
a = list(map(int, input().split()))
a.sort()

def comb(n, r):
    return math.factorial(n) // math.factorial(n - r)

maxi = 0
i = -1
key = a[i] // 2
for j in range(n):
    if a[j] > key:
        break
# print(j, n-1)
# print(j, key, a)
if abs(a[j-1] - key) >= abs(a[j] - key) and j < n-1:
    ans = [a[i], a[j]]
else:
    ans = [a[i], a[j-1]]
# ok = n
# ng = -1
# while abs(ok - ng) > 1:
#     mid = (ok + ng) // 2
#     if key <= a[mid]: ok = mid
#     else: ng = mid
# if ok < i: 
#     if comb(a[i], a[ok]) > maxi:
#         maxi = comb(a[i], a[ok])
#         ans = [a[i], a[ok]]
# if ng >= 0: 
#     if comb(a[i], a[ng]) > maxi:
#         maxi = comb(a[i], a[ng])
#         ans = [a[i], a[ng]]
print("{} {}". format(ans[0], ans[1]))