def growingPlant(upSpeed, downSpeed, desiredHeight):

    if desiredHeight < upSpeed:

        return 1

    height = 0
    day = 1

    while height < desiredHeight:

        height += upSpeed

        if height >= desiredHeight:

            break

        height -= downSpeed
        day += 1

    return day
