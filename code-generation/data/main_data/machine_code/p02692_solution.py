def game_possible(N, A, B, C, choices):
    result = []
    for choice in choices:
        if choice == "AB":
            if A > B:
                A -= 1
                B += 1
                result.append("B")
            else:
                A += 1
                B -= 1
                result.append("A")
        elif choice == "AC":
            if A > C:
                A -= 1
                C += 1
                result.append("C")
            else:
                A += 1
                C -= 1
                result.append("A")
        elif choice == "BC":
            if B > C:
                B -= 1
                C += 1
                result.append("C")
            else:
                B += 1
                C -= 1
                result.append("B")
                
        if A < 0 or B < 0 or C < 0:
            return "No"
        
    return "Yes\n" + "\n".join(result) if A >= 0 and B >= 0 and C >= 0 else "No"