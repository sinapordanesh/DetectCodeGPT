def maximize_groups(n):
    if n < 3:
        return 0
    elif n % 3 == 0:
        return n // 3
    else:
        return n // 3

# Test the function
print(maximize_groups(8))
print(maximize_groups(2))
print(maximize_groups(9))