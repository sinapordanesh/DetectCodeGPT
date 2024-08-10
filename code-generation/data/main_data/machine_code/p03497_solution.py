def rewrite_balls(N, K, A):
    unique_integers = len(set(A))
    if unique_integers <= K:
        return 0
    else:
        return unique_integers - K

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(rewrite_balls(N, K, A))