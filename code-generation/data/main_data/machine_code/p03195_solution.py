def who_wins(N, colors):
    total = sum(colors)
    max_color = max(colors)
    
    if max_color > total - max_color:
        return "first"
    else:
        return "second"