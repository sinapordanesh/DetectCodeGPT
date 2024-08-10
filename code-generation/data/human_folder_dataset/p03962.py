def iroha():
    a, b, c = map(int, input().split())
    if a == b and b == c and a == c:
        print(1)
    elif a != b and b != c and a != c:
        print(3)
    else:
        print(2)

if __name__ == "__main__":
    iroha()

