def symmetric_difference():
    n = int(input())
    set_a = set(map(int, input().split()))
    m = int(input())
    set_b = set(map(int, input().split()))

    symmetric_diff = sorted((set_a - set_b) | (set_b - set_a))

    for num in symmetric_diff:
        print(num)