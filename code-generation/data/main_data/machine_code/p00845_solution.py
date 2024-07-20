def count_stars_visible(n, stars, m, telescopes):
    def angle(x, y):
        dot_product = sum(a*b for a, b in zip(x, y))
        magnitude_x = sum(a**2 for a in x) ** 0.5
        magnitude_y = sum(b**2 for b in y) ** 0.5
        return dot_product / (magnitude_x * magnitude_y)

    stars_visible = set()
    for telescope in telescopes:
        for i, star in enumerate(stars):
            if angle(star, telescope[:3]) > angle(telescope[:3], [0, 0, 0]) - telescope[3]:
                stars_visible.add(i)

    return len(stars_visible)