def number_sorting(A, B, P):
    count = 0
    for i in range(A, B+1):
        for j in range(i, B+1):
            if sorted(str(i)) == sorted(str(j)):
                count += 1
    return count % P