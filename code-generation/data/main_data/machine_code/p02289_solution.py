import heapq

def priority_queue_operations(operations):
    pq = []
    result = []
    
    for operation in operations:
        if operation == 'end':
            break
        elif operation == 'extract':
            result.append(-heapq.heappop(pq))
        else:
            _, num = operation.split()
            heapq.heappush(pq, -int(num))
    
    return result

# Sample Input
operations = ['insert 8', 'insert 2', 'extract', 'insert 10', 'extract', 'insert 11', 'extract', 'extract', 'end']
output = priority_queue_operations(operations)
for item in output:
    print(item)