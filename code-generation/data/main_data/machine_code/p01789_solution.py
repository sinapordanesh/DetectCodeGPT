def unfair_game(N, A, B, heaps):
    
    def xor_sum(arr):
        res = 0
        for num in arr:
            res ^= num
        return res
    
    if A == B:
        if xor_sum(heaps) == 0:
            return "Jiro"
        else:
            return "Hanako"
    
    if A > B:
        return "Hanako"
    else:
        if min(heaps) <= A:
            return "Hanako"
        else:
            return "Jiro"