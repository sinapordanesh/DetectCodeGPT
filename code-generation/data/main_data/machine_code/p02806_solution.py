def playlist_duration(N, songs, X):
    total_duration = 0
    asleep = False
    
    for s, t in songs:
        if s == X:
            asleep = True
        elif asleep:
            total_duration += t
    
    return total_duration

# Sample Input 1
print(playlist_duration(3, [("dwango", 2), ("sixth", 5), ("prelims", 25)], "dwango"))

# Sample Input 2
print(playlist_duration(1, [("abcde", 1000)], "abcde"))

# Sample Input 3
print(playlist_duration(15, [("ypnxn", 279), ("kgjgwx", 464), ("qquhuwq", 327), ("rxing", 549), ("pmuduhznoaqu", 832), ("dagktgdarveusju", 595), ("wunfagppcoi", 200), ("dhavrncwfw", 720), ("jpcmigg", 658), ("wrczqxycivdqn", 639), ("mcmkkbnjfeod", 992), ("htqvkgkbhtytsz", 130), ("twflegsjz", 467), ("dswxxrxuzzfhkp", 989), ("szfwtzfpnscgue", 958)], "pmuduhznoaqu"))