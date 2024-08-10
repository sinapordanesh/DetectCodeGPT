def count_pairs(N):
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                count += 1
    return count

N = int(input())
print(count_pairs(N))