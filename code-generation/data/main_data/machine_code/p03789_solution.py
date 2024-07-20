def min_increasing_integers(N):
    N = str(N)
    count = 0
    for i in range(len(N)):
        if i == 0 or N[i] >= N[i-1]:
            count += int(N[i])
        else:
            count += int(N[i]) - 1
    return count

N = int(input())
print(min_increasing_integers(N))