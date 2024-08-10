def total_gift_worth(N, gifts):
    total = 0
    for gift in gifts:
        if gift[1] == 'JPY':
            total += gift[0]
        else:
            total += gift[0] * 380000.0
    return total

# Sample Input
N = 3
gifts = [(100000000, 'JPY'), (100.00000000, 'BTC'), (0.00000001, 'BTC')]

print(total_gift_worth(N, gifts))