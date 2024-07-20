def smallest_sequence(N, piles):
    ans = [0] * N
    freq = [0] * (max(piles) + 1)
    for i in range(N):
        freq[piles[i]] += 1
    max_stones = max(piles)
    min_index = piles.index(max_stones)
    for i in range(max_stones):
        ans[min_index] += 1
        if i < N - 1:
            if piles[i] == max_stones:
                max_stones = max(piles[i+1:])
                min_index = piles[i+1:].index(max_stones) + i + 1
    return ans

N, *piles = map(int, input().split())
result = smallest_sequence(N, piles)
for res in result:
    print(res)