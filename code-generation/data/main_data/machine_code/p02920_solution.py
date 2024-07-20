def possible_healths(N, S):
    def possible_healths_rec(N, S, idx):
        if idx == 2**N:
            return S == []
        for i in range(len(S)):
            if S[i] == idx:
                if possible_healths_rec(N, S[:i] + S[i+1:], idx+1):
                    return True
        return False

    return "Yes" if possible_healths_rec(N, S, 1) else "No"