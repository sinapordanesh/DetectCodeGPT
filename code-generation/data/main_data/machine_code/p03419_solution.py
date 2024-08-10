def down_cards(N, M):
    return (N * M) // 2

N, M = map(int, input().split())
print(down_cards(N, M))