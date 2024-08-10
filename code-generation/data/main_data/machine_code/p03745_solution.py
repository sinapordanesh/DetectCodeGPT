def min_subarrays(N, A):
    increasing = decreasing = 1
    for i in range(1, N):
        if A[i] > A[i-1]:
            increasing = max(increasing, decreasing + 1)
        elif A[i] < A[i-1]:
            decreasing = max(decreasing, increasing + 1)
    return max(increasing, decreasing)

N = int(input())
A = list(map(int, input().split()))
print(min_subarrays(N, A))