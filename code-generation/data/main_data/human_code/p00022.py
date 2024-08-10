def maxsum(A):
    smax = A[0]
    ssum = max(A[0], 0)
    for a in A[1:]:
        ssum += a
        smax = max(ssum, smax)
        ssum = max(ssum, 0)
    return smax

while True:
    n = int(input())
    if not n:
        break

    A = []
    for i in range(n):
        a = int(input())
        A.append(a)

    print(maxsum(A))