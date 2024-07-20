from typing import List


def answer(a: int, b: int, k: int) -> List[int]:
    a_k = set(range(a, min(a + k, b + 1)))
    k_b = set(range(max(b - k + 1, a + 1), b + 1))

    return sorted(a_k.union(k_b))


def main():
    a, b, k = map(int, input().split())
    for i in answer(a, b, k):
        print(i)


if __name__ == '__main__':
    main()
