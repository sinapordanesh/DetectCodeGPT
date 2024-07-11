def main():
    h, w = map(int, input().split())
    s_list = [list(input().split()) for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if s_list[r][c] == "snuke":
                print(chr(ord("A") + c) + str(r + 1))
                break


if __name__ == "__main__":
    main()
