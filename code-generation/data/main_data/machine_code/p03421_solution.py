def construct_sequence(N, A, B):
    if A + B - 1 > N or A * B < N:
        print(-1)
    else:
        result = []
        for i in range(B):
            result.append(i+1)
        for i in range(N-B):
            result.append(B+i+1)
        for i in range(A+B, N):
            result.append(A+B-N+i+1)
        print(" ".join(map(str, result)))