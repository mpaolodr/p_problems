def longestDigitsPrefix(inputString):

    prefix = list()

    for char in inputString:

        if char.isnumeric():

            prefix.append(char)

        else:

            break

    return "".join(prefix)
