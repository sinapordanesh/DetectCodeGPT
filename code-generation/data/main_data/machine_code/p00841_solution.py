def atomic_car_race(n, checkpoints, b, r, v, e, f):
    def calculate_time(x):
        if x >= r:
            return 1 / (v - e * (x - r))
        else:
            return 1 / (v - f * (r - x))
    
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + b + sum(calculate_time(checkpoints[i-1] - checkpoints[k]) for k in range(j, i)))
    
    return dp[n]


# Sample Input
print(atomic_car_race(2, [2, 3], 1.0, 1, 1.0, 0.1, 0.3))  # Output: 3.5397
print(atomic_car_race(5, [5, 10, 15, 20, 25], 0.15, 1, 1.0, 0.04, 0.5))  # Output: 31.9249
print(atomic_car_race(10, [1783, 3640, 3991, 4623, 5465, 5481, 6369, 6533, 6865, 8425], 4.172, 72, 59.4705, 0.0052834, 0.0611224))  # Output: 168.6682