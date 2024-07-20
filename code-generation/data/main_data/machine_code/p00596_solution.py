def arrange_dominoes(N, subset):
    dominoes = []
    for i in range(7):
        for j in range(i, 7):
            dominoes.append([i, j])
    
    subset = [list(map(int, x)) for x in subset.split()]
    
    for i in range(len(subset)):
        subset[i] = sorted(subset[i])
    
    for i in range(len(dominoes)):
        if dominoes[i] in subset:
            subset.remove(dominoes[i])
    
    if len(subset) == 0:
        return "Yes"
    else:
        return "No"