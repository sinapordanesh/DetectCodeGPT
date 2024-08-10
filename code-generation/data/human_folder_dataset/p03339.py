def count(left_w, right_e):
    return left_w + right_e


def main():
    n = int(input())
    s = str(input())

    w_count = s.count('W')
    e_count = n - w_count

    lst = []
    left = 0
    left_w = 0
    right = n
    right_e = e_count
    for i in range(n):
        s_alp = s[i]
        right -= 1
        if s_alp == 'E':
            right_e -= 1

        lst.append(count(left_w, right_e))

        left += 1
        if s_alp == 'W':
            left_w += 1

    minimum = min(lst)
    print(minimum)


if __name__ == '__main__':
    main()