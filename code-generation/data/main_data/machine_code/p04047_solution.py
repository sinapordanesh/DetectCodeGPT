def max_ingredients(N, skewers):
    skewers.sort()
    total_ingredients = sum(skewers[::2][:N])
    return total_ingredients