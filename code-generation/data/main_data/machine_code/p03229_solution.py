def max_sum_adjacent_diff(N, A):
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += abs(A[i] - A[i-1])
    return ans

N = int(input())
A = list(map(int, input().split()))
print(max_sum_adjacent_diff(N, A))