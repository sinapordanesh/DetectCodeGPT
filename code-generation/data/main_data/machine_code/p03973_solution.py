def max_products_sold(N, cash):
    cash.sort()
    products_sold = 0
    for i in range(N):
        if cash[i] >= products_sold + 1:
            products_sold += 1
    return products_sold