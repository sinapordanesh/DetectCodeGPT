def total_amount(N, prices):
    max_price = max(prices)
    total = sum(prices) - max_price + max_price//2
    return total

#Input
N = 3
prices = [4980, 7980, 6980]

#Function call
print(total_amount(N, prices))