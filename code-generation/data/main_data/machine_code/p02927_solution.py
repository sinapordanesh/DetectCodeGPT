def count_product_days(M, D):
    count = 0
    for m in range(1, M+1):
        for d in range(1, D+1):
            d_1 = d % 10
            d_10 = d // 10
            if d >= 10 and d_1 >= 2 and d_10 >= 2 and d_1 * d_10 == m:
                count += 1
    return count

M, D = map(int, input().split())
print(count_product_days(M, D))