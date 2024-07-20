def blessed_time(logbook):
    total_time = 0
    programmer_start_time = {}
    for i in range(len(logbook)-1):
        if logbook[i][3] == 'I' and logbook[i+1][3] == 'O':
            programmer_id = logbook[i][4]
            start_time = int(logbook[i][1][:2])*60 + int(logbook[i][1][3:])
            end_time = int(logbook[i+1][1][:2])*60 + int(logbook[i+1][1][3:])
            total_time += end_time - start_time
            
            if programmer_id in programmer_start_time:
                programmer_start_time[programmer_id] += end_time - start_time
            else:
                programmer_start_time[programmer_id] = end_time - start_time
    
    max_time = max(programmer_start_time.values())
    return max_time

# Sample Input
logbook = [
    ['04/21', '09:00', 'I', '000'],
    ['04/21', '09:00', 'I', '001'],
    ['04/21', '09:15', 'I', '002'],
    ['04/21', '09:30', 'O', '001'],
    ['04/21', '09:45', 'O', '000'],
    ['04/21', '10:00', 'O', '002'],
    ['04/28', '09:00', 'I', '003'],
    ['04/28', '09:15', 'I', '000'],
    ['04/28', '09:30', 'I', '004'],
    ['04/28', '09:45', 'O', '004'],
    ['04/28', '10:00', 'O', '000'],
    ['04/28', '10:15', 'O', '003'],
    ['04/29', '20:00', 'I', '002'],
    ['04/29', '21:30', 'O', '002']
]

print(blessed_time(logbook))