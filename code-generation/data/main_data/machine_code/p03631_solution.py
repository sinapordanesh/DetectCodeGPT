def check_palindromic_number(N):
    if str(N) == str(N)[::-1]:
        print("Yes")
    else:
        print("No")

#Sample Test Cases
check_palindromic_number(575)
check_palindromic_number(123)
check_palindromic_number(812)