def pass_gates(N, M, gates):
    cards_passed_all_gates = 0
    for card in range(1, N+1):
        for gate in range(M):
            if card < gates[gate][0] or card > gates[gate][1]:
                break
        else:
            cards_passed_all_gates += 1
    return cards_passed_all_gates

# Sample Input 1
print(pass_gates(4, 2, [(1, 3), (2, 4)]))

# Sample Input 2
print(pass_gates(10, 3, [(3, 6), (5, 7), (6, 9)]))

# Sample Input 3
print(pass_gates(100000, 1, [(1, 100000)]))