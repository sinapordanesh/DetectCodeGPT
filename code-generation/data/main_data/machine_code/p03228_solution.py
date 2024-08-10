def cookies(A, B, K):
    for i in range(K):
        if i % 2 == 0:
            if A % 2 == 1:
                A -= 1
            B += A // 2
            A //= 2
        else:
            if B % 2 == 1:
                B -= 1
            A += B // 2
            B //= 2
    return A, B

A, B, K = map(int, input().split())
result = cookies(A, B, K)
print(result[0], result[1])