
from heapq import heapify, heappop


def sort(xs):
    heapify(xs)
    return [heappop(xs) for _ in range(len(xs))]


def run():
    n = int(input())
    elements = []
    for _ in range(n):
        v, w, t, d, s = input().split()
        elements.append((int(v), int(w), t, int(d), s))

    for e in sort(elements):
        print("{} {} {} {} {}".format(*e))


if __name__ == '__main__':
    run()

