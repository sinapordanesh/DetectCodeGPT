def max_consecutive_rainy_days(S):
    count = 0
    max_count = 0
    for char in S:
        if char == 'R':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

# Sample Input 1
print(max_consecutive_rainy_days("RRS"))

# Sample Input 2
print(max_consecutive_rainy_days("SSS"))

# Sample Input 3
print(max_consecutive_rainy_days("RSR"))