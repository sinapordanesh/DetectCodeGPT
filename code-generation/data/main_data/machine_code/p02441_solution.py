def count(b, e, k, A):
    count = 0
    for i in range(b, e):
        if A[i] == k:
            count += 1
    return count

n = int(input())
A = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    b, e, k = map(int, input().split())
    print(count(b, e, k, A))