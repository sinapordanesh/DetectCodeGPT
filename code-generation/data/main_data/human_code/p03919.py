from string import ascii_uppercase


def main(h, w, s):
    h, w = 1, 0  # height, weight

    for row in s:
        for col in row:
            if col == 'snuke':
                print(ascii_uppercase[w] + str(h))
                return
            w += 1

        h += 1
        w = 0


if __name__ == "__main__":
    h, w = map(int, input().split(' '))

    s = [[i for i in input().split(' ')] for _ in range(h)]

    main(h, w, s)
