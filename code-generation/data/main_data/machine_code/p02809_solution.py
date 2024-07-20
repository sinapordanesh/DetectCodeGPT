def arrange_cards(N, a):
    cards = list(range(1, N+1))
    result = []
    
    for i in range(N):
        if i == 0:
            result.append(cards[0])
        else:
            for j in range(1, N+1):
                if j not in result and j != a[result[-1]-1]:
                    result.append(j)
                    break
                    
    if len(result) != N:
        return -1
    else:
        return ' '.join(map(str, result))