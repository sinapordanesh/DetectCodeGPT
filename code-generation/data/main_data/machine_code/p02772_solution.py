def check_immigrant_document(N, numbers):
    for num in numbers:
        if num % 2 == 0 and (num % 3 == 0 or num % 5 == 0):
            continue
        else:
            print("DENIED")
            return
    print("APPROVED")