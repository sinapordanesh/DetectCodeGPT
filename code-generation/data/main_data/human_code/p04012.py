def main():
    w = input()
    d = dict()

    for i in range(len(w)):
        if (w[i] in d):
            d[w[i]] += 1
        else:
            d[w[i]] = 1

    correct = 0
    for v in d.values():
        if v % 2 == 0:
            correct += 1

    if correct == len(d):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
