def earliest_ABC(N):
    while True:
        if len(set(str(N))) == 1:
            return N
        N += 1

N = int(input())
print(earliest_ABC(N))