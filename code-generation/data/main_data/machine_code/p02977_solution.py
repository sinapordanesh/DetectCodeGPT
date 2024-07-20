def tree_with_xor_condition(N):
    if N % 2 == 1:
        print("No")
    else:
        print("Yes")
        for i in range(1, N + 1):
            print(i, i + 1)
        for i in range(N + 1, 2*N - 1):
            print(i, i + 1)

# Sample Input 1
tree_with_xor_condition(3)

# Sample Input 2
tree_with_xor_condition(1)