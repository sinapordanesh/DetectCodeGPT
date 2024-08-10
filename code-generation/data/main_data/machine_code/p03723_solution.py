def cookie_exchange(A, B, C):
    count = 0
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        count += 1
        A, B, C = (B + C) / 2, (A + C) / 2, (A + B) / 2
        if count > 100:
            return -1
    return count

# Sample Input
print(cookie_exchange(4, 12, 20)) # Output: 3
print(cookie_exchange(14, 14, 14)) # Output: -1
print(cookie_exchange(454, 414, 444)) # Output: 1