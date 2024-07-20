def cookies_left(A, B, K):
    for _ in range(K):
        if A > 0:
            A -= 1
        elif B > 0:
            B -= 1
    return A, B

# Sample Input 1
print(cookies_left(2, 3, 3))

# Sample Input 2
print(cookies_left(500000000000, 500000000000, 1000000000000))