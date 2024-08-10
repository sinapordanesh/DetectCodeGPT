def amount_to_hand(N, K, dislikes):
    for i in range(N, 10 ** 4):
        if all(d not in str(i) for d in dislikes):
            return i

N, K = map(int, input().split())
dislikes = list(map(int, input().split()))
print(amount_to_hand(N, K, dislikes))