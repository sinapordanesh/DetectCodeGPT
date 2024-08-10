def minimum_explosions(N, A, B, health):
    explosions = 0
    for h in health:
        h -= A
        explosions += 1
        if h > 0:
            explosions += (h + (A - B) - 1) // (A - B)
    return explosions

# Sample Input 1
print(minimum_explosions(4, 5, 3, [8, 7, 4, 2]))

# Sample Input 2
print(minimum_explosions(2, 10, 4, [20, 20]))

# Sample Input 3
print(minimum_explosions(5, 2, 1, [900000000, 900000000, 1000000000, 1000000000, 1000000000]))