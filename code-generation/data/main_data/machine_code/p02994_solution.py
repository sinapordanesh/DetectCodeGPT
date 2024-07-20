def flavor_of_apple_pie(N, L):
    return (2*L + N - 1) * N // 2 - L

N, L = map(int, input().split())
print(flavor_of_apple_pie(N, L))