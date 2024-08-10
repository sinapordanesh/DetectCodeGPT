def minimize_iterations(s):
    count = 0
    for i in range(16):
        if s[i] != 'CODEFESTIVAL2016'[i]:
            count += 1
    return count

#Sample Input 1
print(minimize_iterations("C0DEFESTIVAL2O16"))

#Sample Input 2
print(minimize_iterations("FESTIVAL2016CODE"))