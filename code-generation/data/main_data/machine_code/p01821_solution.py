def identity_function(N):
    if N == 2:
        return 1
    elif N % 2 == 0:
        return -1
    else:
        return 2

# Test the function with the sample inputs
print(identity_function(3))
print(identity_function(4))
print(identity_function(15))