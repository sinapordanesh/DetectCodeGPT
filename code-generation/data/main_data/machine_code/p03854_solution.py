def obtain_string(S):
    T = ''
    while len(S) > 0:
        if S.endswith('dream'):
            S = S[:-5]
            T += 'dream'
        elif S.endswith('dreamer'):
            S = S[:-7]
            T += 'dreamer'
        elif S.endswith('erase'):
            S = S[:-5]
            T += 'erase'
        elif S.endswith('eraser'):
            S = S[:-6]
            T += 'eraser'
        else:
            return 'NO'
    if S == T:
        return 'YES'
    else:
        return 'NO'