def lowercase_kth_character():
    N, K, S = input().split()
    N = int(N)
    K = int(K)
    S = list(S)
    S[K-1] = S[K-1].lower()
    print(''.join(S))

lowercase_kth_character()