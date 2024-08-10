def escape_from_hell(N, L, drinks, sinners):
    def can_escape(day):
        h = 0
        i = 0
        j = 0
        while i < N and j < day:
            if j % 2 == 0:
                h += drinks[i][0]
            else:
                h -= drinks[i][1]
                h = max(h, 0)
                i += 1
            if h >= L:
                return True
            if j % 2 == 1:
                if h + sinners[j//2] >= L:
                    return False
            j += 1
        return h >= L

    low = 0
    high = N * 2
    while low < high:
        mid = (low + high) // 2
        if can_escape(mid):
            high = mid
        else:
            low = mid + 1

    return high if high <= N * 2 else -1