def digitDegree(n):

    degree = 0

    while n >= 10:

        list_n = list(str(n))

        n = sum([int(char) for char in list_n])

        degree += 1

    return degree
