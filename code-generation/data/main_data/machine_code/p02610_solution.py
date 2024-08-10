def max_camels_happiness(T, cases):
    res = []
    
    for case in cases:
        N = case[0]
        happiness = 0
        
        camels = sorted([(case[i+1], case[i+2], case[i+3]) for i in range(0, 3*N, 3)], reverse=True)
        
        for i in range(N):
            if i < camels[i][0]:
                happiness += camels[i][1]
            else:
                happiness += camels[i][2]
        
        res.append(happiness)
    
    return res

T = 3
cases = [
    [2, 1, 5, 10, 2, 15, 5],
    [3, 2, 93, 78, 1, 71, 59, 3, 57, 96],
    [19, 19, 23, 16, 5, 90, 13, 12, 85, 70, 19, 67, 78, 12, 16, 60, 18, 48, 28, 5, 4, 24, 12, 97, 97, 4, 57, 87, 19, 91, 74, 18, 100, 76, 7, 86, 46, 9, 100, 57, 3, 76, 73, 6, 84, 93, 1, 6, 84, 11, 75, 94, 19, 15, 3, 12, 11, 34]
]

print(max_camels_happiness(T, cases))