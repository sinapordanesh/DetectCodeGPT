def max_possible_amount(N, prices):
    money = 1000
    stocks = 0
    
    for i in range(N-1):
        if prices[i] < prices[i+1]:
            stocks += money // prices[i]
            money %= prices[i]
        else:
            money += stocks * prices[i]
            stocks = 0
    
    money += stocks * prices[N-1]
    
    return money

# Sample Input 1
print(max_possible_amount(7, [100, 130, 130, 130, 115, 115, 150]))

# Sample Input 2
print(max_possible_amount(6, [200, 180, 160, 140, 120, 100]))

# Sample Input 3
print(max_possible_amount(2, [157, 193]))