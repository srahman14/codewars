def make_readable(seconds):
    if seconds <= 59 and len(str(seconds)) == 2: return f"00:00:{seconds}"

    hour = 3600 # one hour is 3600 seconds
    minute = 60 # one minute is 60 seconds
    hours = 0 
    minutes = 0
    if seconds >= 3600:
        hours = seconds / hour
        hours = int(hours)
        seconds = seconds - (hour * hours)

    if seconds < 3600 and seconds >= 60:
        minutes = seconds / minute
        minutes = int(minutes)
        seconds = seconds - (minute * minutes)
    
    if len(str(hours)) == 1:
        hours = "0" + str(hours)

    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)

    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    return f"{hours}:{minutes}:{seconds}"

print(make_readable(60))

# print(10000/3600)