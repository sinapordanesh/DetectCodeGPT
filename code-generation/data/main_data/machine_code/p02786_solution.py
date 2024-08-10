def min_attack_to_win(H):
    count = 0
    while H > 0:
        count += 1
        H = H // 2
    return count

# Test the function with the provided sample inputs
print(min_attack_to_win(2))
print(min_attack_to_win(4))
print(min_attack_to_win(1000000000000))