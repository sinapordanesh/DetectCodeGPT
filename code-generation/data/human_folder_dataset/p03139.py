def LI():
    return list(map(int, input().split()))


N, A, B = LI()
if A+B <= N:
    ans = 0
else:
    ans = A+B-N
print(min(A, B), ans)
