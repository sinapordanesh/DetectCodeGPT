MOD = 10**9 + 7

def count_skewer_meals(N, packs):
    total_ways = 0
    for i in range(N):
        for j in range(i+1, N):
            ways = (2 ** (N - 2)) % MOD
            total_ways = (total_ways + ways) % MOD
    return total_ways

# Sample Input
N = 3
packs = [(1, 1), (1, 1), (2, 1)]

print(count_skewer_meals(N, packs))