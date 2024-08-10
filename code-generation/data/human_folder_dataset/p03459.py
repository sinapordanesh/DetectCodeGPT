# from itertools import product, takewhile
def calc_min_path(current_c, next_c):
    x = abs(current_c[1]-next_c[1])
    y = abs(current_c[2]-next_c[2])
    return x+y


def is_movable(current_c, next_c):
    move_count = next_c[0] - current_c[0]
    min_path = calc_min_path(current_c, next_c)
    if move_count == min_path:
        return True
    if move_count < min_path:
        return False
    if move_count > min_path:
        must_move_count = move_count-min_path
        if must_move_count % 2 == 0:
            return True
        else:
            return False


def main():
    N = int(input())
    coordinate = [[int(x) for x in input().split(" ")] for _ in range(N)]
    coordinate.insert(0, [0, 0, 0])

    for i in range(N):
        if not is_movable(coordinate[i], coordinate[i+1]):
            print("No")
            exit()
    print("Yes")


if __name__ == '__main__':
    main()
