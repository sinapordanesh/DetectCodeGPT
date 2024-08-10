def max_number_of_coins(X, Y, Z, coins):
    coins.sort(key=lambda x: x[0] - x[1])
    gold_total = sum([coin[0] for coin in coins[-X:]])
    silver_total = sum([coin[1] for coin in coins[-Y-Z:-Z]])
    bronze_total = sum([coin[2] for coin in coins[:-Y]])
    return gold_total + silver_total + bronze_total