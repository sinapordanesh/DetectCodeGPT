def guarantee_win(N, piles):
    total = sum(piles)
    if N == 2:
        if (piles[0] - 1) <= (total - piles[0]):
            return piles[0] - 1
        else:
            return -1
    else:
        return -1
        