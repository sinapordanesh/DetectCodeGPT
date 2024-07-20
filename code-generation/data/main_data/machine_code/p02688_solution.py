def snuke_victims():
    N, K = map(int, input().split())
    victims = 0
    for _ in range(K):
        d_i, *A_i = map(int, input().split())
        victims += d_i
    print(N - victims)

snuke_victims()