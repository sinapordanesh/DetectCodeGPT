n = int(input())
A = list(map(int, input().split()))
count = 0


def merge(A, l, m, r):
    L = A[l:m] + [10 ** 9 + 1]
    R = A[m:r] + [10 ** 9 + 1]
    i, j = 0, 0
    for k in range(l, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    global count
    count += r - l


def mergeSort(A, l, r):
    if r - l > 1:
        m = (l + r) // 2
        mergeSort(A, l, m)
        mergeSort(A, m, r)
        merge(A, l, m, r)


mergeSort(A, 0, n)
print(" ".join(list(map(str, A))))
print(count)

