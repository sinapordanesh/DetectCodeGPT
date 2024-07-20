def sum_of_products(N, A):
    P = 200003
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            result += (A[i] * A[j]) % P
    return result

# Sample Input 1
N = 4
A = [2019, 0, 2020, 200002]
print(sum_of_products(N, A))

# Sample Input 2
N = 5
A = [1, 1, 2, 2, 100000]
print(sum_of_products(N, A))