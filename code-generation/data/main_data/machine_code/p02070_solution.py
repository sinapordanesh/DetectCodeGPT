def min_days(N, P, Q):
    def apply_permutation(arr, perm):
        return [arr[p-1] for p in perm]
    
    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    
    d = 0
    while not is_sorted(P):
        P = apply_permutation(P, Q)
        d += 1
        if d > 10**18:
            return -1
    return d