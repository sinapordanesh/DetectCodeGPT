def altar_operations(N, stones):
    count = 0
    for i in range(N):
        if i % 2 == 0 and stones[i] == 'W':
            count += 1
        elif i % 2 == 1 and stones[i] == 'R':
            count += 1
    return count

N = 4
stones = "WWRR"
print(altar_operations(N, stones))

N = 2
stones = "RR"
print(altar_operations(N, stones))

N = 8
stones = "WRWWRWRR"
print(altar_operations(N, stones))