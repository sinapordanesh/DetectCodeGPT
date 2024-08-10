def count_choices_of_K(N):
    count = 0
    for K in range(2, N+1):
        current_N = N
        while current_N >= K:
            if current_N % K == 0:
                current_N /= K
            else:
                current_N -= K
        if current_N == 1:
            count += 1
    return count

N = int(input())
print(count_choices_of_K(N))