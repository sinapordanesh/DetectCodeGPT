def min_flight_time(P, Q, R):
    return min(P+Q, Q+R, R+P)