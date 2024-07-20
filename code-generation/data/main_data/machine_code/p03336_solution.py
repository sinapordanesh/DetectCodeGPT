def calculate_final_numbers(n, m, k, s, t):
    x = int(s, 2)
    y = int(t, 2)
    
    for _ in range(k):
        z = x & y
        x += z
        y += z
    
    return bin(x)[2:], bin(y)[2:]

# Sample Input 1
print(calculate_final_numbers(2, 3, 3, "11", "101"))

# Sample Input 2
print(calculate_final_numbers(5, 8, 3, "10101", "10101001"))

# Sample Input 3
print(calculate_final_numbers(10, 10, 10, "1100110011", "1011001101"))