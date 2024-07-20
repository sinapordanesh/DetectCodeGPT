def handsel(a, b):
    total_money = a + b
    alice_share = total_money // 2
    brown_share = total_money // 2
    return alice_share, brown_share

# Test cases
print(handsel(1000, 3000))
print(handsel(5000, 5000))
print(handsel(1000, 2000))