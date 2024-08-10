import sys

def get_min_value_in_row(data):
    if(len(data) < 1):
        return 0
    min = 0
    for i in range(0,len(data)):
        if(data[i] < data[min]):
            min = i
    return min

def is_max(Min,index,data):
    max = data[index][Min]
    for i in range(index,-1,-1):
        if(data[i][Min] > max):
            max = data[i][Min]
    for i in range(index,len(data)):
        if(data[i][Min] > max):
            max = data[i][Min]
    return True if max == data[index][Min] else False

def print_both(data):
    for i in range(0,len(data)):
        indexmin = get_min_value_in_row(data[i])
        if(is_max(indexmin,i,data) == True):
            print(data[i][indexmin])
            return
    print(0)
    

l = []
for i in sys.stdin:
    l.append(i)

i = 0
while(i < len(l)):
    if(len(l[i]) == 2):
        Matrix = []
        for j in range(i+1,int(l[i])+i+1):
            temp = [l[j].split()]
            for k in range(0,len(temp[0])):
                temp[0][k] = int(temp[0][k])
            Matrix.append(temp[0])
        i += int(l[i]) + 1
        print_both(Matrix)
    else:
        i += 1
