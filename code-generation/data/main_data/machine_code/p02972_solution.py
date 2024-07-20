def find_good_set_of_choices(N, a):
    b = []
    for i in range(1, N+1):
        if a[i-1] == 1:
            b.append(i)
    
    if len(b) == 0:
        print(0)
    else:
        print(len(b))
        for num in b:
            print(num)