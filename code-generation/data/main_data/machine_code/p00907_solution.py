def find_outlier():
    while True:
        degree = int(input())
        if degree == 0:
            break
        values = [float(input()) for _ in range(degree + 3)]
        for i in range(degree + 3):
            if abs(values[i] - sum(x ** i for i, x in enumerate(values[:degree+1]))) > 1.0:
                print(i)

find_outlier()