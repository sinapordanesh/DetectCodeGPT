from typing import List


def answer(n: int, t: int, a: int, hs: List[int]) -> int:
    import sys
    
    result = 0
    temperature_difference = sys.maxsize
    
    for i, h in enumerate(hs, start=1):
        temp = abs(a - (t - h * 0.006))
        if temp < temperature_difference:
            temperature_difference = temp
            result = i

    return result


def main():
    n = int(input())
    t, a = map(int, input().split())
    hs = list(map(int, input().split()))
    print(answer(n, t, a, hs))


if __name__ == '__main__':
    main()