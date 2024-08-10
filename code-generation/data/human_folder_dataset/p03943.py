def iroha():
    li = list(map(int, input().split()))
    li.sort()
    merge = li[0] + li[1]
    if merge == li[2]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    iroha()

