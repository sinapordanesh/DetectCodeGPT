def clocks_pointing_upwards(N, T):
    from math import gcd
    lcm = T[0]
    for i in range(1, N):
        lcm = (lcm * T[i]) // gcd(lcm, T[i])
    return lcm

# Sample Input 1
N = 2
T = [2, 3]
print(clocks_pointing_upwards(N, T))

# Sample Input 2
N = 5
T = [2, 5, 10, 1000000000000000000, 1000000000000000000]
print(clocks_pointing_upwards(N, T))