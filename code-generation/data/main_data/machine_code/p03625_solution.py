def max_rectangle_area(N, sticks):
    sticks.sort()
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                for l in range(k+1, N):
                    if sticks[i] == sticks[j] and sticks[k] == sticks[l]:
                        return sticks[i] * sticks[k]
    return 0