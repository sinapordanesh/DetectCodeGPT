def distribute_hats(N, hats):
    xor = 0
    for i in range(N):
        xor ^= hats[i]
    
    if xor == 0:
        return "Yes"
    else:
        return "No"