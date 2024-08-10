def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

n = int(input())
arr = list(map(int, input().split()))

pivot_index = partition(arr, 0, n-1)

for i in range(n):
    if i == pivot_index:
        print(f"[{arr[i]}]", end=" ")
    else:
        print(arr[i], end=" ")