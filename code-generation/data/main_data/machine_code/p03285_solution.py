def buy_cakes_and_doughnuts(N):
    for i in range(N//4 + 1):
        for j in range(N//7 + 1):
            if (i*4 + j*7) == N:
                return "Yes"
    return "No"