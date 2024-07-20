def stones_to_eat(n, piles):
    total_xor = 0
    min_num = float('inf')
    for pile in piles:
        total_xor ^= pile
        min_num = min(min_num, pile)
    if total_xor == 0:
        return -1
    return sum(pile - total_xor for pile in piles)

# Sample Input 1
print(stones_to_eat(3, [2, 3, 4])) # Output: 3

# Sample Input 2
print(stones_to_eat(3, [100, 100, 100])) # Output: -1