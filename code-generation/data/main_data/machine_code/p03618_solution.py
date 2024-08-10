def count_different_strings(A):
    n = len(A)
    cnt = len(set(A))
    
    if n == cnt:
        return n
    elif n == 2 and A[0] == A[1]:
        return 1
    else:
        return min(n, cnt + 2)

A = input()
print(count_different_strings(A))