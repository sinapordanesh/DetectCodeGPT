def print_test_cases():
    case_number = 1
    while True:
        x = int(input())
        if x == 0:
            break
        print(f"Case {case_number}: {x}")
        case_number += 1

print_test_cases()