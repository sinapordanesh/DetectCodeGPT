def check_string(S):
    if S[0] == 'A' and S.count('C') == 1 and S[2:-1].islower():
        return 'AC'
    else:
        return 'WA'