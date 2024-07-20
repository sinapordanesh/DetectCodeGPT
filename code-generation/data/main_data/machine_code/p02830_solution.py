def alternate_strings():
    N = int(input())
    S, T = input().split()

    result = ''
    for i in range(N):
        result += S[i] + T[i]

    print(result)