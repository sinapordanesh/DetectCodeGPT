def find_intersection():
    n = int(input())
    set_a = set(map(int, input().split()))
    m = int(input())
    set_b = set(map(int, input().split()))

    intersection = set_a.intersection(set_b)

    for num in sorted(intersection):
        print(num)