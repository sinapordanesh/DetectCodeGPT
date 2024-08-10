def study_hours(T, X):
    return T / X

T, X = map(int, input().split())
print("{:.10f}".format(study_hours(T, X)))