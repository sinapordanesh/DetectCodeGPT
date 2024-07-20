def main():
    N = int(input())
    s = input()

    if s.count("R") > s.count("B"):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()