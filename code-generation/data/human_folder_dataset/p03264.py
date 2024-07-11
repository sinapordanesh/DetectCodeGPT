from itertools import combinations


def main():
    n = int(input())

    ans = 0
    for a, b in (list(combinations(range(1, n+1), 2))):
        if (a%2==0 and b%2 != 0) or (b%2==0 and a%2!=0):
            ans += 1

    print(ans)


main()