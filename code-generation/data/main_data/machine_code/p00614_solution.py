def ideal_coin_payment(p, coins):
    total_coins = 0
    for i in range(5, -1, -1):
        change_coins = min(p // coins[i], coins[i])
        p -= change_coins * coins[i]
        total_coins += change_coins
    return total_coins

# Input
data = [
    [123, [1, 5, 10, 50, 100, 500]],
    [999, [9, 9, 9, 9, 9, 9]],
    [0, [0, 0, 0, 0, 0, 0]]
]

for d in data:
    if d[0] == 0:
        pass
    else:
        print(ideal_coin_payment(d[0], d[1]))