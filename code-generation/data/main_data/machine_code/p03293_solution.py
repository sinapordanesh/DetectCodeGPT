def check_rotation(S, T):
    if len(S) != len(T):
        return 'No'
    else:
        for i in range(len(S)):
            if S == T:
                return 'Yes'
            S = S[-1] + S[:-1]
        return 'No'