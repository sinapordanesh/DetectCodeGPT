def beautiful_currency(N, coins):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    max_ratio = 0
    for i in range(N - 1):
        ratio = (coins[i + 1] - coins[i]) / coins[i]
        max_ratio = max(max_ratio, ratio)
    
    result = 0
    for i in range(N - 1):
        ratio = (coins[i + 1] - coins[i]) / coins[i]
        result = max(result, ratio / max_ratio)
    
    return result

# Test the function
print(beautiful_currency(3, [6, 11, 12]))
print(beautiful_currency(3, [6, 11, 24]))
print(beautiful_currency(3, [6, 11, 30]))