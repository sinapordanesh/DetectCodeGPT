def harshad_number(N):
    f_X = sum([int(i) for i in str(N)])
    if N % f_X == 0:
        print("Yes")
    else:
        print("No")