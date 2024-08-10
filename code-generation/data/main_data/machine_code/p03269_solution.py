def construct_graph(L):
    N = 2 * L - 1
    M = 3 * L - 3
    
    print(N, M)
    
    for i in range(1, N):
        print(i, i+1, 0)
    
    for i in range(2, N - 1, 2):
        print(i, i+2, 1)
    
    for i in range(1, L-1):
        print(i, i+2, i)
    
# Sample Input 1
construct_graph(4)

# Sample Input 2
construct_graph(5)