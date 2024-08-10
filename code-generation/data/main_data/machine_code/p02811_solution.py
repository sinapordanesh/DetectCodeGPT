def coins_add_up_to_x(K, X):
    total = K * 500
    if total >= X:
        print("Yes")
    else:
        print("No")

# Read input from stdin
K, X = map(int, input().split())

# Call the function with the given input
coins_add_up_to_x(K, X)