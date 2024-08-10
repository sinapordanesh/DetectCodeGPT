from typing import List


def answer(n: int, a: List[int]) -> int:
    alice = 0
    bob = 0

    a.sort(reverse=True)
    for i in range(0, len(a), 2):
        alice += a[i]
    for j in range(1, len(a), 2):
        bob += a[j]

    return abs(alice - bob)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(answer(n,a))


if __name__ == '__main__':
    main()
