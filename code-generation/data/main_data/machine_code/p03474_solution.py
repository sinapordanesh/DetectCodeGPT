def postal_code_format(A, B, S):
    if len(S) != A + B + 1:
        return "No"
    
    if S[A] != "-":
        return "No"
    
    for i in range(len(S)):
        if i != A and not S[i].isdigit():
            return "No"
    
    return "Yes"