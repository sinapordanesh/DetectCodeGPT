def find_multiples(N, S, W, Q):
    a = [0]*N
    g = S
    count = 0
    
    for i in range(N):
        a[i] = (g//7) % 10
        if g % 2 == 0:
            g = g//2
        else:
            g = g//2 ^ W
    
    for i in range(N):
        num = 0
        for j in range(i, N):
            num = num*10 + a[j]
            if a[i] != 0 and num % Q == 0:
                count += 1
    
    return count

# Read input values
inputs = []
while True:
    N, S, W, Q = map(int, input().split())
    if N == 0 and S == 0 and W == 0 and Q == 0:
        break
    inputs.append((N, S, W, Q))

# Calculate and output results
for inp in inputs:
    print(find_multiples(*inp))