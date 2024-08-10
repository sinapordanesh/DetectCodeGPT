def ferris_wheel_cost(A, B):
    if A >= 13:
        return B
    elif 6 <= A <= 12:
        return B // 2
    else:
        return 0

# Sample Input 1
print(ferris_wheel_cost(30, 100))

# Sample Input 2
print(ferris_wheel_cost(12, 100))

# Sample Input 3
print(ferris_wheel_cost(0, 100))