def can_permute_to_multiple_of_4(N, a):
    count = 0
    for i in range(N):
        if a[i] % 4 == 0:
            count += 1
    
    if count >= N - 1:
        return "Yes"
    else:
        return "No"