# A - ringring
def main():
    abc = list(map(int, input().split()))
    abc.sort()
    cnt = 0

    for _ in range(2):
        cnt += abc.pop(0)
    else:
        print(cnt)


if __name__ ==  "__main__":
    main()