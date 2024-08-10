def qualification_contests(N, A, B, S):
    japanese_passed = 0
    overseas_passed = 0
    for i in range(N):
        if S[i] == 'a' and japanese_passed < A+B:
            print("Yes")
            japanese_passed += 1
        elif S[i] == 'b' and japanese_passed < A+B and overseas_passed < B:
            print("Yes")
            japanese_passed += 1
            overseas_passed += 1
        else:
            print("No")

# Sample Input 1
qualification_contests(10, 2, 3, "abccabaabb")

# Sample Input 2
qualification_contests(12, 5, 2, "cabbabaacaba")

# Sample Input 3
qualification_contests(5, 2, 2, "ccccc")