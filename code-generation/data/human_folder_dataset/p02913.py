n = int(input())
s = str(input())

def z_algorithm(s):
    n = len(s)
    Z = [0]*n
    Z[0] = n
    i = 1
    j = 0
    while i < n:
        while i+j < n and s[j] == s[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < n and k+Z[k] < j:
            Z[i+k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z

ans = 0
for i in range(n):
    t = s[i:]
    z = z_algorithm(t)
    for j in range(len(z)):
        if z[j] <= j:
            ans = max(ans, z[j])
print(ans)
