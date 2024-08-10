def main():
    a, b = map(int, input().split())
    num_neg = 0
    if a <= 0 and b >= 0:
        print('Zero')
        return
    elif a > 0:
        print('Positive')
        return
    else:
        num_neg = b - a
        if num_neg % 2 == 1:
            print('Positive')
            return
        else:
            print('Negative')
            return


if __name__ == '__main__':
    main()
