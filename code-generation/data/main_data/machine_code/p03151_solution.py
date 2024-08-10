def pass_exams(N, A, B):
    C = [max(a, b) for a, b in zip(A, B)]
    if sum(A) > sum(C):
        return -1
    else:
        return sum(a != c for a, c in zip(A, C))

# Test the function with sample input
print(pass_exams(3, [2, 3, 5], [3, 4, 1]))
print(pass_exams(3, [2, 3, 3], [2, 2, 1]))
print(pass_exams(3, [17, 7, 1], [25, 6, 14]))
print(pass_exams(12, [757232153, 372327760, 440075441, 195848680, 354974235, 458054863, 463477172, 740174259, 615762794, 632963102, 529866931, 64991604], [74164189, 98239366, 465611891, 362739947, 147060907, 118867039, 63189252, 78303147, 501410831, 110823640, 122948912, 572905212]))