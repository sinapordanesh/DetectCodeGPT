def count_ways(N, S):
    count = 0
    for i in range(1, 2**len(S)):
        red = ""
        blue = ""
        for j in range(len(S)):
            if i & (1 << j):
                red += S[j]
            else:
                blue += S[j]
        if red == blue[::-1]:
            count += 1
    return count

N = int(input())
S = input()
print(count_ways(N, S))