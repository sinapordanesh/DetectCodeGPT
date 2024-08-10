def RabbitLunch(M, N, m0, md, n0, nd):
    m = [m0]
    n = [n0]
    for i in range(1, max(M, N) + 1):
        m.append((m[i - 1] * 58 + md) % (N + 1))
        n.append((n[i - 1] * 58 + nd) % (M + 1))
    
    rabbits = min([min(m[i], n[i]) for i in range(1, min(M, N) + 1)])
    
    return rabbits

# Test the function
print(RabbitLunch(2, 3, 1, 3, 1, 0))
print(RabbitLunch(5, 8, 1, 2, 3, 4))