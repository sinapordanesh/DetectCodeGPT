def min_coins(n):
    coins = [25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += n // coin
        n %= coin
    return num_coins

n = int(input())
print(min_coins(n))