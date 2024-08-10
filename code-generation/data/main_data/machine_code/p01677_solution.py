def recover_audio_signal(datasets):
    output = []
    
    for data in datasets:
        N = int(data[0])
        signal = data[1]
        
        broken_indices = [i for i in range(N) if signal[i] == 'x']
        broken_values = [signal[i] for i in broken_indices]
        
        possible_values = set()
        
        for i in broken_indices:
            left = signal[i-1] if i-1 >= 0 else None
            right = signal[i+1] if i+1 < N else None
            
            if left is not None and right is not None:
                if (left == 'x' or signal[i] - 1 > left) and (right == 'x' or signal[i] + 1 < right):
                    possible_values.add(signal[i] - 1)
                    possible_values.add(signal[i] + 1)
            elif left is not None:
                if left == 'x' or signal[i] - 1 > left:
                    possible_values.add(signal[i] - 1)
            elif right is not None:
                if right == 'x' or signal[i] + 1 < right:
                    possible_values.add(signal[i] + 1)
            else:
                possible_values.add(1)
        
        if len(possible_values) == 1:
            output.append(possible_values.pop())
        elif len(possible_values) == 0:
            output.append("none")
        else:
            output.append("ambiguous")
    
    return output

# Read input datasets
datasets = []
while True:
    N = int(input())
    if N == 0:
        break
    signal = input().split()
    datasets.append((N, signal))

# Call the function and print the output
output = recover_audio_signal(datasets)
for val in output:
    print(val)