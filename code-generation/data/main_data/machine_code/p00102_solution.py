def matrix_computation():
    while True:
        n = int(input())
        if n == 0:
            break
        matrix = []
        row_sums = [0] * n
        col_sums = [0] * n
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
            for i in range(n):
                row_sums[_] += row[i]
                col_sums[i] += row[i]
        
        for i in range(n):
            row_str = ' '.join('{:5d}'.format(num) for num in matrix[i])
            row_sum_str = '{:5d}'.format(row_sums[i])
            print(row_str, row_sum_str)
        
        col_sum_str = ' '.join('{:5d}'.format(num) for num in col_sums)
        print(col_sum_str)

matrix_computation()