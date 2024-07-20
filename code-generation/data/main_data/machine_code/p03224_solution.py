def tuple_of_subsets(N):
    if N % 2 == 0:
        print("Yes")
        print(N)
        for i in range(1, N+1):
            print("2", i, (i % N) + 1)
    else:
        print("No")