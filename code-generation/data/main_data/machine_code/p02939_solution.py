def max_partition(S):
    count = 1
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            count += 1
    return count

S = input()
print(max_partition(S))