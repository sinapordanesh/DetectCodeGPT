def find_rain_received(N, A):
    rain_received = [0]*N
    for i in range(N):
        rain_received[i] = A[i-1] - sum(rain_received) - rain_received[(i+1)%N]
    return rain_received

# Sample Input 1
print(*find_rain_received(3, [2, 2, 4])) 

# Sample Input 2
print(*find_rain_received(5, [3, 8, 7, 5, 5]))

# Sample Input 3
print(*find_rain_received(3, [1000000000, 1000000000, 0]))