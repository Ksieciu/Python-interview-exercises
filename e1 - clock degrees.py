def clock_diff(hour, minutes):
    if hour >= 12:
        hour -= 12
    hour_degrees = hour * 30 + 0.5 * minutes
    minutes_degrees = 6 * minutes
    degrees_diff = abs(hour_degrees - minutes_degrees)
    if degrees_diff > 180:
        degrees_diff = 360 - degrees_diff
    return degrees_diff

time = input("Write time in format proper format(ex. 00:00): ")
hour, minutes = time.split(':')
hour = int(hour)
minutes = int(minutes)

if hour >= 24 or minutes >= 60:
    print("Wrong time input!")
else:
    print(clock_diff(hour, minutes), "degrees")
