def truncate_string(K, S):
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + "...")