def buy_energy_drinks(N, M, AB):
    AB.sort(key=lambda x: x[0])
    ans = 0
    for a, b in AB:
        if b >= M:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    return ans

# Sample Input 1
print(buy_energy_drinks(2, 5, [[4, 9], [2, 4]]))

# Sample Input 2
print(buy_energy_drinks(4, 30, [[6, 18], [2, 5], [3, 10], [7, 9]]))

# Sample Input 3
print(buy_energy_drinks(1, 100000, [[1000000000, 100000]]))