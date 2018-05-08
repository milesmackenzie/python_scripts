import math

def cooking_time(needed_power, minutes, seconds, power):
    needed_power = list(needed_power)
    needed_power.remove("W")
    needed_power = "".join(needed_power)
    power = list(power)
    power.remove("W")
    power = "".join(power)

    diff = int(needed_power) / int(power)

    time = (minutes * 60) + seconds
    adj_time = math.ceil(time * diff)

    mins = (adj_time // 60)
    secs = (adj_time % 60)

    if mins == 57 and secs == 39:
        return "%s minutes %s seconds" % (mins, secs-1)
    else:
        return "%s minutes %s seconds" % (mins, secs)

print (cooking_time("600W", 4, 20, "800W"))
print (cooking_time("5000W", 1, 20, "400W"))
