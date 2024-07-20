def min_operations(N, A):
    B = list(map(int, input().split()))
    
    count = 0
    for i in range(N):
        if A[N+i] == B[i]:
            continue
        else:
            idx = A.index(B[i])
            A.pop(idx)
            count += abs(N + i - idx)
    
    if A == B:
        return count
    else:
        return -1

N = int(input())
A = list(map(int, input().split()))

print(min_operations(N, A))