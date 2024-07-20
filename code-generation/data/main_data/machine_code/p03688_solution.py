def cat_hats(N, a):
    a.sort()
    if a[0] == a[-1] or a[-1] > sum(a[:-1]):
        return "No"
    return "Yes"