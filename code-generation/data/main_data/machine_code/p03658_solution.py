def max_length_of_toy(N, K, sticks):
    sticks.sort(reverse=True)
    return sum(sticks[:K])