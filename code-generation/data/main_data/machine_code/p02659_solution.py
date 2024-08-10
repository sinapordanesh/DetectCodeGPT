def compute_product(A, B):
    result = int(A * float(B))
    print(result)

# Read input values
A, B = input().split()
A = int(A)
B = float(B)

# Call the function with input values
compute_product(A, B)