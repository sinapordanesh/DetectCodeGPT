#!/usr/bin/env python


def solve(A: int, B: int, K: int):
    if A >= K:
        return f"{A-K} {B}"
    elif A + B >= K:
        return f"0 {A+B-K}"
    else:
        return "0 0"


def main():
    A, B, K = map(int, input().split())
    answer = solve(A, B, K)
    print(answer)


if __name__ == "__main__":
    main()
