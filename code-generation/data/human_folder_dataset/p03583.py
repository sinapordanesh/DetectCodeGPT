import sys

def cal():
    N = int(input())

    for i in range(1, 3501):
        for j in range(1, 3501):
            num0 = 4*i*j-N*(i+j) 
            if num0 != 0:
                num = N*i*j/num0
                if num.is_integer() and 0 < num <= 3500:
                    print(i, int(num), j)
                    sys.exit()

cal()
