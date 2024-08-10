def min_different_characters(N, A):
    return max(A) - (N - 1) 

N = 3
A = [3, 2, 1]
print(min_different_characters(N, A))

N = 5
A = [2, 3, 2, 1, 2]
print(min_different_characters(N, A))