def study_period(H1, M1, H2, M2, K):
    start_time = H1 * 60 + M1
    end_time = H2 * 60 + M2
    period_length = end_time - start_time - K
    return max(period_length, 0) * 1

# Sample Input 1
print(study_period(10, 0, 15, 0, 30))

# Sample Input 2
print(study_period(10, 0, 12, 0, 120))