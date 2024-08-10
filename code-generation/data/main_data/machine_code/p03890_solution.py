def kode_festival(N, hardness):
    while N > 0:
        for i in range(0, len(hardness), 2):
            if hardness[i] > hardness[i+1]:
                hardness[i] -= hardness[i+1]
                hardness.pop(i+1)
            elif hardness[i] < hardness[i+1]:
                hardness[i+1] -= hardness[i]
                hardness.pop(i)
            N -= 1
    return hardness[0]