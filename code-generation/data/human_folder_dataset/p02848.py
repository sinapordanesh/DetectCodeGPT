#!/usr/bin/env python3


def solve(N: int, S: str):
    answer = ""
    for s in S:
        answer += chr(65 + (ord(s) - 65 + N) % 26)
    return answer


def main():
    N = int(input())
    S = input().strip()
    answer = solve(N, S)
    print(answer)


if __name__ == "__main__":
    main()
