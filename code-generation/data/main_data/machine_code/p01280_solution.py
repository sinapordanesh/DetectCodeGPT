def max_volume_access(N, planets):
    for planet in planets:
        max_volume = max(planet[2:])
        print(max_volume)