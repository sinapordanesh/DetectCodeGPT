def calculate_saving(n, prices):
    coins = 0
    spent = 0
    for i in range(n):
        if prices[i] >= 500 and prices[i] % 500 == 0:
            coins += prices[i] // 500
            spent += prices[i]
        else:
            change = 1000 - (prices[i] % 1000)
            if change == 500:
                coins += 1
                spent += prices[i] + change
            else:
                coins += 1
                spent += prices[i] + change
    return coins, spent

# Input
datasets = []
while True:
    n = int(input())
    if n == 0:
        break
    prices = []
    for _ in range(n):
        prices.append(int(input()))
    datasets.append((n, prices))

# Output
for n, prices in datasets:
    c, s = calculate_saving(n, prices)
    print(c, s)