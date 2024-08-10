def reorder_sequence(N, A, B):
    count = {}
    for i in range(N):
        if A[i] not in count:
            count[A[i]] = 0
        count[A[i]] += 1
        if B[i] not in count:
            count[B[i]] = 0
        count[B[i]] -= 1

    if all(val >= 0 for val in count.values()):
        print("Yes")
        print(" ".join(str(x) for x in B))
    else:
        print("No")