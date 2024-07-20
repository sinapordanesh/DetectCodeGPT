def max_operations(N, s):
    count = 0
    for i in range(1, N-1):
        if s[i-1] == "1" and s[i] == "0" and s[i+1] == "1":
            count += 1
            s = s[:i-1] + "0" + s[i+1:]
    return count

# Sample Input 1
print(max_operations(7, "1010101"))

# Sample Input 2
print(max_operations(50, "10101000010011011110001001111110000101010111100110"))