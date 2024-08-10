def bisect_right_rev(lst, x):
    if lst[0] < x:
        return 0
    if x <= lst[-1]:
        return len(lst)

    a = 0
    b = len(lst) - 1

    while abs(b - a) > 1:
        c = (a + b) // 2

        if lst[c] < x:
            b = c
        else:
            a = c
    
    return b

N = int(input())
A = [int(input()) for _ in range(N)]
seq = []

for i in range(N):
    if len(seq) == 0:
        seq.append(A[i])
    else:
        ind = bisect_right_rev(seq, A[i])
        if ind == len(seq):
            seq.append(A[i])
        else:
            seq[ind] = A[i]

print(len(seq))