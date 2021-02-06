def validTime(time):

    time_list = time.split(":")

    hour = int(time_list[0])
    minutes = int(time_list[1])

    if 0 <= hour <= 23 and 0 <= minutes <= 59:

        return True

    return False
