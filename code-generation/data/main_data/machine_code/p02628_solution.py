def min_total_price(N, K, prices):
    prices.sort()
    return sum(prices[:K])