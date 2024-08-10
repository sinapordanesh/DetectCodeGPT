import sys

def sumItUp(List):
    result = []
    for i in range(0,len(List)):
        result.append(sum(List[0:i+1]))
    return sum(result)

List = []
for i in sys.stdin:
    List.append(i)

for i in range(1,len(List),2):
    List[i] = List[i].split()
    for j in range(0,len(List[i])):
        List[i][j] = int(List[i][j])
    List[i] = sorted(List[i])
    print(sumItUp(List[i]))
