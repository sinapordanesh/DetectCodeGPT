def reverse_sort(N, A):
    count = 0
    for i in range(N-1):
        if A[i] != i + 1:
            j = A.index(i+1)
            A[i:j+1] = A[i:j+1][::-1]
            count += 1
    return count

N = int(input())
A = list(map(int, input().split()))
print(reverse_sort(N, A))