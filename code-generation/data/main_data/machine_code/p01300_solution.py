def count_11_sequences(num):
    count = 0
    for i in range(len(num)):
        for j in range(i+1, len(num)+1):
            if int(num[i:j]) % 11 == 0:
                count += 1
    return count

while True:
    num = input()
    if num == '0':
        break
    print(count_11_sequences(num))