def buy_ice_tea(Q, H, S, D, N):
    total_cost = 0
    
    if N % 2 == 0:
        total_cost = min(Q*2, H, S*2, D) * (N // 2)
    else:
        total_cost = min(Q*(N % 2)*2, H*(N % 2), S*(N % 2)*2, D) + min(Q*2, H, S*2, D) * (N // 2)
    
    return total_cost

# Test the function with the provided sample inputs
print(buy_ice_tea(20, 30, 70, 90, 3))
print(buy_ice_tea(10000, 1000, 100, 10, 1))
print(buy_ice_tea(10, 100, 1000, 10000, 1))
print(buy_ice_tea(12345678, 87654321, 12345678, 87654321, 123456789))