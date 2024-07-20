def introduce_restaurants(N, restaurants):
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for i in range(N):
        print(restaurants[i][2])

# Sample Input
N = 6
restaurants = [("khabarovsk", 20, 1), ("moscow", 10, 2), ("kazan", 50, 3), ("kazan", 35, 4), ("moscow", 60, 5), ("khabarovsk", 40, 6)]
introduce_restaurants(N, restaurants)