def number_of_subsequences(n, seq):
    mod = 10**9 + 7
    count = [0] * (n + 2)
    pos = [-1] * (n + 2)
    last = -1
    for i in range(n + 1):
        j = seq[i]
        count[i + 1] = (count[i] + (i - pos[j])) % mod
        if pos[j] != -1:
            last = pos[j]
        pos[j] = i

    inc = count[n + 1] - count[last]
    for i in range(1, n + 2):
        ans = (count[i] + inc) % mod
        print(ans)

# Sample Input
number_of_subsequences(3, [1, 2, 1, 3])