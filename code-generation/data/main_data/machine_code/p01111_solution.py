def skyscraper_rental_plan():
    while True:
        budget = int(input())
        if budget == 0:
            break
        total = 0
        i = 1
        while total + i <= budget:
            total += i
            i += 1
        print(f"1 {i-1}")

skyscraper_rental_plan()