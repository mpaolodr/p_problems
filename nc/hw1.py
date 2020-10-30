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

# Libby Thomas Solution
# def csSchoolYearsAndGroups(years, groups):

#     results = ["1a", "1b"]

#     for x in range(1, years + 1):

#         year_num = x
#         year_list = []
#         year_list.append(year_num)

#         for y in range(1, groups + 1):

#             group_letter = chr(ord("`") + y)
#             group_list = []
#             group_list.append(group_letter)

#             for number in year_list:

#                 for letter in group_list:

#                     another_list = []
#                     year_and_group = "%d%s" % (number, letter)
#                     another_list.append(year_and_group)
#                     results.append(another_list[0])

#     return ", ".join(results)


print(csSchoolYearsAndGroups(700, 25))


def csMakeItJazzy(chords):

    for i in range(len(chords)):

        if chords[i][-1] != "7":

            chords[i] = chords[i] + "7"

    return chords


# def csMakeItJazzy(chords):

#     alpha = ["a", "b"]

#     new_c = [f"{c}7" if c[-1] !=
#              "7" else c for c in chords if c.startswith("G")]

    return new_c


print(csMakeItJazzy(["G7", "E", "F7"]))
