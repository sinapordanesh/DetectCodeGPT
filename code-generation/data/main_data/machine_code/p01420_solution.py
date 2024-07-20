def marathon_match(N, M, L, runners):
    def win_probability(p, t, v):
        return t / (v * L)

    probabilities = []
    for runner in runners:
        p, t, v = runner
        probability = win_probability(p, t, v)
        probabilities.append(probability)
    
    return probabilities