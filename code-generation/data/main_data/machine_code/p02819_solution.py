def minimum_prime(X):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    while True:
        if is_prime(X):
            return X
        X += 1

X = int(input())
print(minimum_prime(X))