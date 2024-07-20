def check_parallel(n, datasets):
    for dataset in datasets:
        x1, y1, x2, y2, x3, y3, x4, y4 = dataset
        if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1):
            print("YES")
        else:
            print("NO")

# Sample Input
n = 2
datasets = [(0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 2.0, 1.0), 
            (3.0, 2.0, 9.0, 6.0, 13.0, 5.0, 7.0, 9.0)]

check_parallel(n, datasets)