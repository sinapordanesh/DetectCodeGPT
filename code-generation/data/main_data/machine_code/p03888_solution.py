def equivalent_resistance(R1, R2):
    R3 = 1 / (1/R1 + 1/R2)
    return R3

R1, R2 = map(int, input().split())
print("{:.10f}".format(equivalent_resistance(R1, R2)))