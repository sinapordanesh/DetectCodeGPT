def rabbit_party(n, m, pairs):
    happiness = [0] * (n + 1)
    for u, v, f in pairs:
        happiness[u] = max(happiness[u], f)
        happiness[v] = max(happiness[v], f)
    
    return sum(happiness)

# Sample Input 1
n = 3
m = 3
pairs = [(1, 2, 3), (2, 3, 1), (3, 1, 2)]
print(rabbit_party(n, m, pairs))

# Sample Input 2
n = 2
m = 1
pairs = [(1, 2, 5)]
print(rabbit_party(n, m, pairs))

# Sample Input 3
n = 1
m = 0
pairs = []
print(rabbit_party(n, m, pairs))

# Sample Input 4
n = 4
m = 5
pairs = [(1, 2, 4), (1, 3, 3), (2, 3, 7), (2, 4, 5), (3, 4, 6)]
print(rabbit_party(n, m, pairs))