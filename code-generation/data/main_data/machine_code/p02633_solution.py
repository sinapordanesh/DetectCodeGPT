import math

def min_actions_to_start(X):
    return 360 // math.gcd(360, X)

X = int(input())
print(min_actions_to_start(X))