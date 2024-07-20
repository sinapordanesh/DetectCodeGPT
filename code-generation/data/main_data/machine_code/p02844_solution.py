def count_pin_codes(N, S):
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                pin = S[i] + S[j] + S[k]
                if int(pin) % 2 == 0:
                    count += 1
    return count

N = int(input())
S = input()
print(count_pin_codes(N, S))