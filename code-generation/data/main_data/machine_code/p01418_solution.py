def sleeping_time(K, R, L, P, E, T):
    def calc_prob(K, R, L, P, E, T, prob):
        if K == 0:
            if abs((R + L) / 2 - T) <= E:
                return prob
            else:
                return 0
        else:
            H = (R + L) / 2
            prob_correct = calc_prob(K - 1, R, H, P, E, T, prob * (1 - P))
            prob_incorrect = calc_prob(K - 1, H, L, P, E, T, prob * P)
            return prob_correct + prob_incorrect

    return round(calc_prob(K, R, L, P, E, T, 1), 6)