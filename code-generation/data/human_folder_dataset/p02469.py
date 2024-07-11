# coding=utf-8


def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    if n1 == n2 or n2 == 0:
        return n1
    n1, n2 = n2, (n1 % n2)
    return gcd(n1, n2)


def lcm(n1, n2):
    return n1*n2//gcd(n1, n2)


def multi_lcm(numbers_list):
    if len(numbers_list) == 2:
        return lcm(numbers_list[0], numbers_list[1])
    elif len(numbers_list) > 2:
        numbers_list2 = [lcm(numbers_list[0], numbers_list[1])]
        numbers_list2.extend(numbers_list[2:])
        return multi_lcm(numbers_list2)


if __name__ == '__main__':
    n = int(input())
    number_list = list(map(int, input().split()))
    print(multi_lcm(number_list))

