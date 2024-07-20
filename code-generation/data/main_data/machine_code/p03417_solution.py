def count_cards_facing_down(N, M):
    return (N * M) // 2

N, M = map(int, input().split())
print(count_cards_facing_down(N, M))