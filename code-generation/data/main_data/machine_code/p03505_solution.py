def contests_to_kaiden(K, A, B):
    rating = 0
    contests = 0
    while rating < K:
        contests += 1
        if contests % 2 == 1:
            rating += A
        else:
            rating -= B
        if rating >= K:
            return contests
    return -1

K, A, B = map(int, input().split())
print(contests_to_kaiden(K, A, B))