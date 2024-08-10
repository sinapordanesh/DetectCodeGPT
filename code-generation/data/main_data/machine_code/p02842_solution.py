def find_apple_pie_price(N):
    for X in range(1, N+1):
        if X * 1.08 == N:
            return X
    return ":("

# Read input from Standard Input
N = int(input().strip())

# Call the function and print the output
print(find_apple_pie_price(N))