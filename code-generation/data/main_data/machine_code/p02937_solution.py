def min_concatenation(s, t):
    n = len(s)
    m = len(t)
    if m > n:
        return -1
    i = (m * pow(10, 100)) // (n - m)
    while (pow(10, 100) * n) % (n - m) != 0:
        i += 1
    return i

# Sample Input 1
print(min_concatenation("contest", "son"))

# Sample Input 2
print(min_concatenation("contest", "programming"))

# Sample Input 3
print(min_concatenation("contest", "sentence"))