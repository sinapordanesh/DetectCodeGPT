def generate_smallest_string(N, strings):
    s, t = strings
    L = len(s) * len(t)
    q, r = divmod(N, L)
    
    if r == 0:
        return min(s * q + t * q, t * q + s * q)
    else:
        return min(s * (q+1) + t * q, t * (q+1) + s * q) if s > t else min(s * q + t * (q+1), t * q + s * (q+1))