def alternatingSums(a):

    if len(a) == 1:

        return [a[0], 0]

    if len(a) == 2:

        return [a[0], a[1]]

    pointer = 0

    team_a = list()
    team_b = list()

    while pointer < len(a):

        team_a.append(a[pointer])

        pointer += 2

    pointer = 1

    while pointer < len(a):

        team_b.append(a[pointer])

        pointer += 2

    return [sum(team_a), sum(team_b)]
