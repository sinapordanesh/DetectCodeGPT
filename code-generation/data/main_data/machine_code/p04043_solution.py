def construct_haiku(A, B, C):
    if A+B+C == 17 and A != B and B != C and A != C:
        return "YES"
    else:
        return "NO" 

# Sample Input 1
print(construct_haiku(5, 5, 7))

# Sample Input 2
print(construct_haiku(7, 7, 5))