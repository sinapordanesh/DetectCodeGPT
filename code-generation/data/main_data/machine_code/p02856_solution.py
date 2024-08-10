def max_rounds(M, contestants):
    total_rounds = 0
    while contestants > 9:
        total_rounds += 1
        contestants = int(str(contestants).replace('0', '')) - 1
    return total_rounds

# Sample Input 1
print(max_rounds(2, 229))

# Sample Input 2
print(max_rounds(3, 1000000007))