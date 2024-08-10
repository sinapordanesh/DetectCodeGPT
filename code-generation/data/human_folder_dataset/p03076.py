import math


def main():
    t = []
    for i in range(5):
        t.append(int(input()))

    max_wait = 0
    max_wait_order = 0
    for i in range(len(t)):
        if t[i] % 10 != 0 and 10 - (t[i] % 10) >= max_wait:
            max_wait = 10 - t[i] % 10
            max_wait_order = i

    time = 0
    for i in range(len(t)):
        if i == max_wait_order:
            continue
        else:
            time += math.ceil(t[i] / 10) * 10
    time += t[max_wait_order]

    print(time)


if __name__ == '__main__':
    main()
