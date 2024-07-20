def min_coins(N, prices):
    total_price = sum(prices)
    coins = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000, 100000000000]
    
    count = 0
    for coin in coins[::-1]:
        count += total_price // coin
        total_price %= coin
    
    return count

# Sample Input 1
print(min_coins(3, [43, 24, 37]))

# Sample Input 2
print(min_coins(5, [49735011221, 970534221705, 411566391637, 760836201000, 563515091165]))