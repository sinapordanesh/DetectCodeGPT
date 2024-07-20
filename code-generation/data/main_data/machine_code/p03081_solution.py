def remaining_golems(N, Q, s, spells):
    golems = [1] * N
    for t, d in spells:
        for i in range(N):
            if s[i] == t:
                if d == "L" and i > 0:
                    golems[i-1] += golems[i]
                    golems[i] = 0
                elif d == "R" and i < N-1:
                    golems[i+1] += golems[i]
                    golems[i] = 0
    return sum(golems)