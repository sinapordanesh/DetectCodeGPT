def can_pay_exactly(N, A):
    if N % 500 <= A:
        print("Yes")
    else:
        print("No")

# Test the function with sample inputs
can_pay_exactly(2018, 218)
can_pay_exactly(2763, 0)
can_pay_exactly(37, 514)