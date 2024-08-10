def eventual_length_of_X(X):
    while "ST" in X:
        X = X.replace("ST", "", 1)
    return len(X)