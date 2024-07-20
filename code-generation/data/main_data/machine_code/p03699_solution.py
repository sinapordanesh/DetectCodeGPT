def max_grade(N, scores):
    total = sum(scores)
    if total % 10 == 0:
        return total - min(scores)
    return total

# Sample Input 1
print(max_grade(3, [5, 10, 15])) 

# Sample Input 2
print(max_grade(3, [10, 10, 15])) 

# Sample Input 3
print(max_grade(3, [10, 20, 30]))