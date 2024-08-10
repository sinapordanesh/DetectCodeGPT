def AddMulSubDiv(N, Q, L, R, A, queries):
    count = 0
    for q in queries:
        if q[0] == 1:
            x, s, t = q[1], q[2], q[3]
            for i in range(len(A)):
                if A[i] >= x:
                    A[i] = t * (A[i] + s)
        elif q[0] == 2:
            x, s, t = q[1], q[2], q[3]
            for i in range(len(A)):
                if A[i] <= x:
                    A[i] = int((A[i] - s) / t)
        count += len([ele for ele in A if L <= ele <= R])
    return count

# Sample Input
print(AddMulSubDiv(3, 3, 3, 10, [1, -2, 3], [[1, 2, 2, 3], [2, 20, 1, 3], [2, 1, 20, 5]]))