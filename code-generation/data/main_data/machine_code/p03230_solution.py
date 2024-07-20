def tuple_of_subsets(N):
    if N % 2 == 1:
        print("No")
    else:
        print("Yes")
        print(N)
        for i in range(1, N+1):
            print(2, i, i % N + 1)

N = int(input())
tuple_of_subsets(N)