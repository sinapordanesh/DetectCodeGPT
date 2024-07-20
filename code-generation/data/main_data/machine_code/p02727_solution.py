def max_deliciousness(X, Y, A, B, C, p, q, r):
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)
    
    eaten = p[:X] + q[:Y]
    eaten.sort(reverse=True)
    
    total = sum(eaten)
    
    idx_p = X
    idx_q = Y
    idx_r = 0
    
    while idx_r < C and r[idx_r] > eaten[-1]:
        total -= eaten[-1]
        total += r[idx_r]
        idx_r += 1
        eaten.pop()
    
    return total

# Sample Input 1
print(max_deliciousness(1, 2, 2, 2, 1, [2, 4], [5, 1], [3]))

# Sample Input 2
print(max_deliciousness(2, 2, 2, 2, 2, [8, 6], [9, 1], [2, 1]))

# Sample Input 3
print(max_deliciousness(2, 2, 4, 4, 4, [11, 12, 13, 14], [21, 22, 23, 24], [1, 2, 3, 4]))