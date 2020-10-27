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
