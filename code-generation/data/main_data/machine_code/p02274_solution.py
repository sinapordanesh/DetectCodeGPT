def count_inversions(n, arr):
    cnt = 0
    for i in range(n):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                cnt += 1
    return cnt

n = int(input())
arr = list(map(int, input().split()))
print(count_inversions(n, arr))