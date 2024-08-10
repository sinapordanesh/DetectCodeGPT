def lowest_cost():
    while True:
        amount = int(input())
        if amount == 0:
            break
        
        if amount % 500 == 0:
            cost_a = (amount // 200) * 380 * 0.8
            cost_b = (amount // 300) * 550 * 0.85
            cost_c = (amount // 500) * 850 * 0.88
            print(min(cost_a, cost_b, cost_c))

lowest_cost()