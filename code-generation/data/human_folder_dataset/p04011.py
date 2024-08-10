def iroha():
    n, k, price, special = [int(input()) for i in range(4)]
    result = 0
    for i in range(n):
        if i < k:
            result += price
        else:
            result += special
    print(result)

if __name__ == "__main__":
    iroha()
