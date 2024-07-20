def max_x_value(N, S):
    x = 0
    max_x = 0
    for i in range(N):
        if S[i] == 'I':
            x += 1
        elif S[i] == 'D':
            x -= 1
        max_x = max(max_x, x)
    return max_x

# Sample Input 1
print(max_x_value(5, "IIDID")) # Output: 2

# Sample Input 2
print(max_x_value(7, "DDIDDII")) # Output: 0