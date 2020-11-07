def isLucky(n):

    # convert to string
    to_string = str(n)

    first_half = [int(n) for n in to_string[:len(to_string) // 2]]
    second_half = [int(n) for n in to_string[len(to_string) // 2:]]

    if sum(first_half) == sum(second_half):

        return True

    return False
