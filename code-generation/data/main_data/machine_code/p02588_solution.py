def count_integer_product(N, A):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            product = A[i] * A[j]
            if product.is_integer():
                count += 1
    return count

N = int(input())
A = [float(input()) for _ in range(N)]
print(count_integer_product(N, A))