def train_ticket(ticket_number):
    A = int(ticket_number[0])
    B = int(ticket_number[1])
    C = int(ticket_number[2])
    D = int(ticket_number[3])
    
    if A + B + C + D == 7:
        print(str(A) + "+" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
    elif A + B + C - D == 7:
        print(str(A) + "+" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
    elif A + B - C + D == 7:
        print(str(A) + "+" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
    elif A + B - C - D == 7:
        print(str(A) + "+" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
    elif A - B + C + D == 7:
        print(str(A) + "-" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
    elif A - B + C - D == 7:
        print(str(A) + "-" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
    elif A - B - C + D == 7:
        print(str(A) + "-" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
    elif A - B - C - D == 7:
        print(str(A) + "-" + str(B) + "-" + str(C) + "-" + str(D) + "=7")

# Sample Input
train_ticket("1222")
train_ticket("0290")
train_ticket("3242")