def max_final_value(T):
    x = 0
    for i in range(len(T)):
        if T[i] == '1':
            x += i % 2 + 1
    return x

# Sample Test Cases
print(max_final_value("1101"))
print(max_final_value("0111101101"))