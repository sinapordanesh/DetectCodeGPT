def possible_obtain(S):
    while len(S) > 0:
        if S.endswith("dream"):
            S = S[:-5]
        elif S.endswith("dreamer"):
            S = S[:-7]
        elif S.endswith("erase"):
            S = S[:-5]
        elif S.endswith("eraser"):
            S = S[:-6]
        else:
            return "NO"
    return "YES" 

S = input().strip()
print(possible_obtain(S))