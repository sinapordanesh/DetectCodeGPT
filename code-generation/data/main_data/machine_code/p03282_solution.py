def mr_infinity_string(S, K):
    days = 5 * 10**15
    while days > 0:
        new_S = ""
        for digit in S:
            if digit == '1':
                new_S += '1'
            else:
                new_S += digit*(int(digit))
        S = new_S
        days -= 1
    
    return S[K-1]