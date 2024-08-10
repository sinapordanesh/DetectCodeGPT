def min_study_hours(N, X, info):
    def check(t):
        A = sum(max(l, min(u, t + b)) * c for c, l, u, b in info)
        B = sum(max(l, min(u, b)) * c for c, l, u, b in info)
        return A >= B
    
    left = 0
    right = X
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid
    
    return right

# Read input
N, X = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
print(min_study_hours(N, X, info))