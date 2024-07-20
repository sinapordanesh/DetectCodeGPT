def determine_grades(N, K, A):
    for i in range(K, N):
        if A[i] > A[i - 1]:
            print("Yes")
        else:
            print("No")