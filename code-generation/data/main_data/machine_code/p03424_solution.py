def arare_bag(N, arare_colors):
    if len(set(arare_colors)) == 3:
        return "Three"
    else:
        return "Four"