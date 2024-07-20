def is_good(N):
    N = str(N)
    for i in range(len(N)-2):
        if N[i] == N[i+1] == N[i+2]:
            return "Yes"
    return "No"

# Sample Input 1
print(is_good(1118)) # Output: Yes

# Sample Input 2
print(is_good(7777)) # Output: Yes

# Sample Input 3
print(is_good(1234)) # Output: No