# coding=utf-8


def vector_minus(v1, v2):
    return [elm1 - elm2 for elm1, elm2 in zip(v1, v2)]


def scalar_multi(scalar, vector):
    return [scalar*elm for elm in vector]


def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    if n1 == n2 or n2 == 0:
        return n1
    n1, n2 = n2, (n1 % n2)
    return gcd(n1, n2)


def solve_int(number1, number2):
    """
    answer1 = 1
    while True:
        if (1+number1*answer1) % number2 == 0:
            return -answer1, (1+number1*answer1)//number2
        answer1 += 1
    """
    if number1 < number2:
        if number1 == 1:
            return 1, 0
        reverse_flag = 1
        n1, n2 = number2, number1
    else:
        if number2 == 1:
            return 0, 1
        reverse_flag = 0
        n1, n2 = number1, number2

    quotient1 = []
    coeff1 = [1, 0]
    quotient2 = []
    coeff2 = [0, 1]

    while True:
        quotient1.append(n1//n2)
        coeff1 = vector_minus(coeff1, scalar_multi(n1//n2, coeff2))
        if n1 % n2 == 1:
            if reverse_flag:
                return coeff1[1], coeff1[0]
            else:
                return coeff1[0], coeff1[1]

        r_memo = n1 % n2
        quotient2.append(n2//r_memo)
        coeff2 = vector_minus(coeff2, scalar_multi(n2//r_memo, coeff1))
        if n2 % r_memo == 1:
            if reverse_flag:
                return coeff2[1], coeff2[0]
            else:
                return coeff2[0], coeff2[1]

        n1, n2 = n1 % n2, n2 % r_memo


def modify_solution(x_sp_s, y_sp_s, n1, n2):
    x_memo, y_memo = x_sp_s, y_sp_s
    if abs(x_sp_s + n2) + abs(y_sp_s - n1) < (abs(x_memo) + abs(y_memo)):
        m = y_sp_s//n1
        if m == 0:
            return x_sp_s+n2, y_sp_s-n1
        return modify_solution(x_sp_s + m*n2, y_sp_s - m*n1, n1, n2)
    if abs(x_sp_s + n2) + abs(y_sp_s - n1) == (abs(x_memo) + abs(y_memo)):
        pass
    return x_memo, y_memo


if __name__ == '__main__':
    a, b = map(int, input().split())
    right_side = gcd(a, b)
    if right_side > 1:
        a //= right_side
        b //= right_side

    x_sp, y_sp = solve_int(a, b)
    if x_sp > y_sp:
        m2 = x_sp//b
        x_sp -= (m2+1)*b
        y_sp += (m2+1)*a
    x_sp, y_sp = modify_solution(x_sp, y_sp, a, b)
    print(x_sp, y_sp)

