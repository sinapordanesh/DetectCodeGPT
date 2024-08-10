def min_time_to_light_candles(N, K, candles):
    distance = []
    for i in range(N - K + 1):
        distance.append(candles[i + K - 1] - candles[i] + min(abs(candles[i]), abs(candles[i + K - 1])))
    return min(distance)