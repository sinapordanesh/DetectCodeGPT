def stones_to_eat(N, piles):
    total_stones = sum(piles)
    min_stones_to_eat = 0
    for pile in piles:
        if (total_stones - pile) % 2 == 0:
            min_stones_to_eat += 1
    if min_stones_to_eat == total_stones:
        return -1
    return min_stones_to_eat