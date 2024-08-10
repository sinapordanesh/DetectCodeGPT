def min_possible_score(N, K, A, F):
    def calc_time(a, f):
        return (a - min(a, K)) * f
    
    member_sort = sorted(range(N), key=lambda x: A[x], reverse=True)
    food_sort = sorted(range(N), key=lambda x: F[x])
    
    ans = float('inf')
    for i in range(N+1):
        for j in range(N-i+1):
            t = 0
            for k in range(i):
                t += calc_time(A[member_sort[k]], F[food_sort[k]])
            for k in range(j):
                t += calc_time(A[member_sort[N-k-1]], F[food_sort[N-k-1]])
            for k in range(i, N-j):
                t += min(calc_time(A[member_sort[k]], F[food_sort[k]]), calc_time(A[member_sort[N-k-1]], F[food_sort[N-k-1]]))
            ans = min(ans, t)
    
    return ans

# Input
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

# Output
print(min_possible_score(N, K, A, F))