def max_yen(N, gemstones):
    max_yen = 0
    for i in range(1, N+1):
        count = 0
        for j in range(i, N+1, i):
            if gemstones[j-1] > 0:
                count += 1
        if count % 2 == 1:
            max_yen += abs(gemstones[i-1])
    return max_yen

N = 6
gemstones = [1, 2, -6, 4, 5, 3]
print(max_yen(N, gemstones))

N = 6
gemstones = [100, -100, -100, -100, 100, -100]
print(max_yen(N, gemstones))

N = 5
gemstones = [-1, -2, -3, -4, -5]
print(max_yen(N, gemstones))

N = 2
gemstones = [-1000, 100000]
print(max_yen(N, gemstones))