def print_integers(A, B, K):
    for i in range(A, B+1):
        if i <= A+K-1 or i >= B-K+1:
            print(i)

# Sample Input 1
print_integers(3, 8, 2)

# Sample Input 2
print_integers(4, 8, 3)

# Sample Input 3
print_integers(2, 9, 100)