def min_max_sum():
    n = int(input())
    array = list(map(int, input().split()))
    print(min(array), max(array), sum(array))

min_max_sum()