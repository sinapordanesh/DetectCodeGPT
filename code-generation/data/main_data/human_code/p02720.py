def main():
    K = int(input()) 

    lunlun = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    start1 = ["1"]
    start2 = ["2"]
    start3 = ["3"]
    start4 = ["4"]
    start5 = ["5"]
    start6 = ["6"]
    start7 = ["7"]
    start8 = ["8"]
    start9 = ["9"]

    while len(lunlun) < 10 ** 5:
        next_starts = []
        for i in range(1, 10):
            news = []
            if i == 1:
                for n in start1:
                    if len(n) == 1:
                        new_n = n + "0"
                    else:
                        if abs(int(n[0])) > 1 or abs(int(n[1])) > 1:
                            break
                        new_n = n[0] + "0" + n[1:]
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start1:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start2:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 2:
                for n in start1:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start2:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start3:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 3:
                for n in start2:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start3:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start4:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 4:
                for n in start3:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start4:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start5:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 5:
                for n in start4:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start5:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start6:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 6:
                for n in start5:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start6:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start7:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 7:
                for n in start6:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start7:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start8:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 8:
                for n in start7:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start8:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start9:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)
            elif i == 9:
                for n in start8:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                for n in start9:
                    new_n = str(i) + n
                    lunlun.append(new_n)
                    news.append(new_n)
                next_starts.append(news)

        start1 = next_starts[0]
        start2 = next_starts[1]
        start3 = next_starts[2]
        start4 = next_starts[3]
        start5 = next_starts[4]
        start6 = next_starts[5]
        start7 = next_starts[6]
        start8 = next_starts[7]
        start9 = next_starts[8]

    print(lunlun[K-1])

main()

