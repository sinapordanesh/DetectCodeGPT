def restaurant_payment(N):
    x = N * 800
    y = (N // 15) * 200
    return x - y

# For Sample Input 1
print(restaurant_payment(20))

# For Sample Input 2
print(restaurant_payment(60))