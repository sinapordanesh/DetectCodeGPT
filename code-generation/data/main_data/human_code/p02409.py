import sys


def main():
    n = int(sys.stdin.readline())
    notices = []
    for i in range(n):
        notices.append(tuple(map(int, sys.stdin.readline().split())))
    buildings = [[[0] * 10 for i in range(3)] for j in range(4)]
    for b, f, r, v in notices:
        buildings[b-1][f-1][r-1] += v
    separator = '####################'
    for index, building in enumerate(buildings):
        for floor in building:
            print(' ' + ' '.join(map(str, floor)))
        if index != len(buildings)-1:
            print(separator)
    return


if __name__ == '__main__':
    main()

