def can_participate(S):
    wins = S.count('o')
    if wins + (15 - len(S)) >= 8:
        return "YES"
    else:
        return "NO"