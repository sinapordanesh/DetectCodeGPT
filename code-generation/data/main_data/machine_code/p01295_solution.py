def champernowne_constant(N, K):
    constant = "0." + "".join(str(i) for i in range(1, 10**6))
    return constant[N:N+K]

# Input
inputs = []
while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    inputs.append((N, K))

# Output
for N, K in inputs:
    print(champernowne_constant(N, K))