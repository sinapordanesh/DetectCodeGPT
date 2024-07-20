def f(A, B):
    def xor(x):
        if x % 4 == 0:
            return x
        if x % 4 == 1:
            return 1
        if x % 4 == 2:
            return x + 1
        return 0
    
    return xor(B) ^ xor(A-1) if A > 0 else xor(B)