def largest_perfect_power(X):
    for i in range(int(X ** 0.5), 0, -1):
        for j in range(2, int(X ** 0.5) + 1):
            if i ** j <= X:
                return i ** j

X = int(input())
print(largest_perfect_power(X))