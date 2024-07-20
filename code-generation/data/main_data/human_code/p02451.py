n = int(input())
a = list(map(int, input().split(' ')))

def binary_search(val):
    left, right = 0, n-1
    while right - left >= 0:
        mid = int((right+left)/2)
        if a[mid] == val: return 1
        if a[mid] < val:
            left = mid+1
        elif val < a[mid]:
            right = mid-1
    return 0

q = int(input())
for i in range(q):
    k = int(input())
    print(binary_search(k))

