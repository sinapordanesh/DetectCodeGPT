def minimize_cable_length(N, a, b):
    mod = 10**9 + 7
    a.sort()
    b.sort()
    ans = 1
    for i in range(N):
        ans = (ans * (N + i)) % mod
    return ans

# Sample Input
N = 2
a = [0, 10]
b = [20, 30]
print(minimize_cable_length(N, a, b))

N = 3
a = [3, 10, 8]
b = [7, 12, 5]
print(minimize_cable_length(N, a, b))