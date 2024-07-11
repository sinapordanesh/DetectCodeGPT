from typing import List


def answer(n: int, d: List[int]) -> int:
    return len(set(d))

def main():
    n = int(input())
    d = list(int(input()) for _ in range(n))
    print(answer(n,d))

if __name__ == '__main__':
    main()