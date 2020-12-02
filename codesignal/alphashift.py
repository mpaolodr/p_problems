def alphabeticShift(inputString):

    to_string = list(inputString)

    for i in range(len(to_string)):

        if to_string[i] == "z":

            to_string[i] = "a"

        else:

            to_string[i] = chr(ord(to_string[i]) + 1)

    return "".join(to_string)
