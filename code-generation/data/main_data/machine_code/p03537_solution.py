def is_palindrome_possible(S, N, operations):
    def apply_operation(S, L, R):
        new_S = list(S)
        for i in range(L-1, R):
            new_S[i] = chr((ord(new_S[i]) - ord('a') + 1) % 26 + ord('a'))
        return "".join(new_S)
    
    for i in range(N):
        L, R = operations[i]
        S = apply_operation(S, L, R)
    
    return "YES" if S == S[::-1] else "NO"