import string


def csWhereIsBob(names):

    for index, val in enumerate(names):

        if val == "Bob":

            return index

    return -1


def csAlphanumericRestriction(input_str):

    # check if all characters is alphabet
    if input_str.isalpha() or input_str.isnumeric():

        return True

    return False


def csOppositeReverse(txt):

    upper = set(string.ascii_uppercase)
    lower = set(string.ascii_lowercase)

    new_txt = ""

    for char in txt[::-1]:

        if char in upper:

            new_txt += char.lower()

        elif char in lower:

            new_txt += char.upper()

        else:

            new_txt += char

    return new_txt


def csSquareAllDigits(n):

    result = ""

    to_string = str(n)

    for char in to_string:

        to_int = int(char)

        result += str(to_int ** 2)

    return int(result)


def csSchoolYearsAndGroups(years, groups):

    res = list()
    lowercase = list(string.ascii_lowercase)

    for y in range(1, years + 1):

        for g in range(1, groups + 1):

            res.append(f"{y}{lowercase[g - 1]}")

    return ", ".join(res)
