def check_sequences(N, a, b):
    for i in range(N):
        if a[i] > b[i]:
            return "No"
    return "Yes" 

# Sample Input 1
print(check_sequences(3, [1, 2, 3], [5, 2, 2])) # Yes

# Sample Input 2
print(check_sequences(5, [3, 1, 4, 1, 5], [2, 7, 1, 8, 2])) # No

# Sample Input 3
print(check_sequences(5, [2, 7, 1, 8, 2], [3, 1, 4, 1, 5])) # No