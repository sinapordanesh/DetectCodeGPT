def check_poor_triple(A, B, C):
    if A == B and A != C:
        print("Yes")
    elif A == C and A != B:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    else:
        print("No") 

# Test the function
check_poor_triple(5, 7, 5)
check_poor_triple(4, 4, 4)
check_poor_triple(4, 9, 6)
check_poor_triple(3, 3, 4)