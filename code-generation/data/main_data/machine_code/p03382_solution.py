def maximize_comb(n, a):
    max_val = 0
    selected = (0, 0)
    for i in range(n):
        for j in range(i):
            val = (a[i] * (a[i] - 1)) // 2
            if val > max_val:
                max_val = val
                selected = (a[i], a[j])
    return selected[0], selected[1]