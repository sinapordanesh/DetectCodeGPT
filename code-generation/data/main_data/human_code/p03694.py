def minimum_dist(l1: list) -> int:
    return max(l1) - min(l1)


if __name__ == "__main__":
    n = int(input())
    list_coordinate = list(map(int, input().split()))
    print(minimum_dist(list_coordinate))
