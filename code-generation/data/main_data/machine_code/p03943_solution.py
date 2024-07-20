def distribute_candy(a, b, c):
    total = a + b + c
    if total % 2 == 0 and total // 2 in [a, b, c]:
        return "Yes"
    else:
        return "No"