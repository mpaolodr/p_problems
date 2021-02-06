def sumUpNumbers(inputString):

    new_str = ""

    for char in inputString:

        if char.isnumeric():

            new_str += char

        else:

            new_str += " "

    total = 0

    for elem in new_str.split():

        num = extractNum(elem)

        print(elem)

        if num.isnumeric():

            total += int(num)

    return total


def extractNum(elem):

    num = ""

    for char in elem:

        if char.isnumeric():

            num += char

    return num
