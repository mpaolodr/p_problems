def electionsWinners(votes, k):

    leading = max(votes)

    chances = 0
    num_leading = 0

    for vote in votes:

        if vote + k > leading:

            chances += 1

        if vote == leading:

            num_leading += 1

    if chances == 0 and num_leading > 1:

        return 0

    elif chances == 0 and num_leading == 1:

        return 1

    return chances
