def find_sequence(K):
    if K % 2 == 0:
        N = 2
        largest = K // 2
        a = [largest, largest]
    else:
        N = 3
        largest = (K + 1) // 2
        a = [largest - 1, 0, largest]
        
    print(N)
    print(" ".join(str(num) for num in a))