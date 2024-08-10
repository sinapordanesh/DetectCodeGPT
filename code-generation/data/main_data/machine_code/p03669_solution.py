def jigsaw_arrangement(N, H, pieces):
    def possible(arrangement):
        bottom = [0] * (H + 1)
        for i, (H, A, B, C, D) in arrangement:
            if bottom[H] < C + H:
                return False
            bottom[A] = max(bottom[A], C + H)
            bottom[B] = max(bottom[B], D + H)
        return True
    
    arrangement = [(H, A, B, C, D) for A, B, C, D in pieces]
    if possible(arrangement):
        return "YES"
    return "NO"