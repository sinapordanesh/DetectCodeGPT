def stone_game(n, k, m):
    stones = list(range(1, n + 1))
    current = m - 1
    while len(stones) > 1:
        del stones[current]
        current = (current + k - 1) % len(stones)
    return stones[0]

# Sample Input
print(stone_game(8, 5, 3))
print(stone_game(100, 9999, 98))
print(stone_game(10000, 10000, 10000))