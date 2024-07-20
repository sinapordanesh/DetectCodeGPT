def shellSort(A, n):
    cnt = 0
    m = int(n**0.5) # calculate m value
    G = []
    h = 1
    while h <= n:
        G.append(h)
        h = 3*h + 1
    G = G[::-1]
    
    for i in range(m):
        insertionSort(A, n, G[i])
    
    return A, cnt

def insertionSort(A, n, g):
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

sorted_A, cnt = shellSort(A, n)
print(len(G))
print(*G)
print(cnt)
print(*sorted_A)