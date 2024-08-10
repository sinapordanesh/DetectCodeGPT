def min_attacks(N, K, health):
    max_health = max(health)
    total_attacks = sum(h - max_health for h in health if h > max_health)
    return total_attacks + min(K, max_health)

# Input
N, K = map(int, input().split())
health = list(map(int, input().split()))

# Output
print(min_attacks(N, K, health))