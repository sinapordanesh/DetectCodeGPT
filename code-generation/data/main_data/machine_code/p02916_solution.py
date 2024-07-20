def satisfaction_points():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    total_satisfaction = B[A[0]-1]

    for i in range(1, N):
        total_satisfaction += B[A[i]-1]
        if A[i] == A[i-1] + 1:
            total_satisfaction += C[A[i-1]-1]

    print(total_satisfaction)

satisfaction_points()