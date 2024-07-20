def happiness_difference(N, dishes):
    dishes.sort(key=lambda x: x[1] + x[0], reverse=True)
    takahashi_points = sum(dish[0] for dish in dishes[::2])
    aoki_points = sum(dish[1] for dish in dishes[1::2])
    return takahashi_points - aoki_points

#Input
N = 3
dishes = [(10, 10), (20, 20), (30, 30)]

print(happiness_difference(N, dishes))

N = 3
dishes = [(20, 10), (20, 20), (20, 30)]

print(happiness_difference(N, dishes))

N = 6
dishes = [(1, 1000000000), (1, 1000000000), (1, 1000000000), (1, 1000000000), (1, 1000000000), (1, 1000000000)]

print(happiness_difference(N, dishes))