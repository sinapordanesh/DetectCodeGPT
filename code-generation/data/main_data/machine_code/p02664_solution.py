def max_doctoral_postdoctoral_quotient(T):
    return T.replace('?', 'D')

#Sample Input 1
print(max_doctoral_postdoctoral_quotient("PD?D??P"))

#Sample Input 2
print(max_doctoral_postdoctoral_quotient("P?P?"))