def selection_sort(A):
    swaps = 0
    for i in range(len(A)):
        mini = i
        for j in range(i, len(A)):
            if A[j] < A[mini]:
                mini = j
        if i != mini:
            A[i], A[mini] = A[mini], A[i]
            swaps += 1
    return A, swaps

# Input
N = int(input())
A = list(map(int, input().split()))

# Output
sorted_A, swaps = selection_sort(A)
print(*sorted_A)
print(swaps)