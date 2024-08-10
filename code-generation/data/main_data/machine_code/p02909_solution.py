def predict_weather_tomorrow(S):
    if S == "Sunny":
        return "Cloudy"
    elif S == "Cloudy":
        return "Rainy"
    else:
        return "Sunny"