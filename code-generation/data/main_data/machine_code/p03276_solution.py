def min_time_to_light_candles(N, K, x):
    time = 0
    for i in range(K-1, N):
        if i == N-1:
            time += abs(x[i]-x[i-K+1])
        else:
            time += min(abs(x[i]-x[i-K+1]), abs(x[i]-x[i+1]))
    return time

# Sample Input 1
print(min_time_to_light_candles(5, 3, [-30, -10, 10, 20, 50]))

# Sample Input 2
print(min_time_to_light_candles(3, 2, [10, 20, 30]))

# Sample Input 3
print(min_time_to_light_candles(1, 1, [0]))

# Sample Input 4
print(min_time_to_light_candles(8, 5, [-9, -7, -4, -3, 1, 2, 3, 4]))