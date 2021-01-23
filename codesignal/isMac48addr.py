def isMAC48Address(inputString):

    if len(inputString) > 17 or len(inputString) < 17:

        return False

    to_list = inputString.split("-")

    for pair in to_list:

        try:

            num = int(pair, base=16)

            if num < 0 or num > 255:

                return False

        except ValueError:

            return False

    return True
