def find_multiple_of_K(K):
    for i in range(1, K+1):
        if int('7'*i) % K == 0:
            return i
    return -1

K = int(input())
print(find_multiple_of_K(K))