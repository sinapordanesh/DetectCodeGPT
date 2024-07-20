def find_inner_rating(N, R):
    if N >= 10:
        return R
    else:
        return R + 100 * (10 - N) 

#Sample Input 1
print(find_inner_rating(2, 2919))

#Sample Input 2
print(find_inner_rating(22, 3051))