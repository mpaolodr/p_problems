def deleteDigit(n):

    to_string = str(n)
    max_possible = 0

    for i in range(len(to_string)):

        max_possible = max(max_possible, int(
            to_string[:i] + to_string[i + 1:]))

    return max_possible
