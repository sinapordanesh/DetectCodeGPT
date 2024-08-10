def find_a_k(N, K, p, q):
    def f(p, q):
        return [q[i-1] for i in p]
    
    a = [p, q]
    while len(a) < K:
        a.append(f(a[-2], a[-1]))
    
    return a[K-1]