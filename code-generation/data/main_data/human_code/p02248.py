def compute_prefix_function(p):
    m = len(p)
    pi = [0 for _ in range(m + 1)]
    pi[1] = 0
    k = 0
    for q in range(2, m + 1):
        while k > 0 and p[k] != p[q - 1]:
            k = pi[k]
        if p[k] == p[q - 1]:
            k += 1
        pi[q] = k
    return pi


def kmp_matcher(t, p):
    n = len(t)
    m = len(p)
    pi = compute_prefix_function(p)
    q = 0
    for i in range(1, n + 1):
        while q > 0 and p[q] != t[i - 1]:
            q = pi[q]
        if p[q] == t[i - 1]:
            q += 1
        if q == m:
            print(i - m)
            q = pi[q]


t = input()
p = input()
kmp_matcher(t, p)
