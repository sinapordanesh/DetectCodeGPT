def choose_integers(n, k):
    if k <= n//2 + n%2:
        return "YES"
    else:
        return "NO"