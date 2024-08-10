def chocolate_pieces(N, D, X, A):
    remaining = X
    for i in range(N):
        remaining += (D-1) // A[i] + 1
    return remaining

#Sample Input 1
print(chocolate_pieces(3, 7, 1, [2, 5, 10]))

#Sample Input 2
print(chocolate_pieces(2, 8, 20, [1, 10]))

#Sample Input 3
print(chocolate_pieces(5, 30, 44, [26, 18, 81, 18, 6]))