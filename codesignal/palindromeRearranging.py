def palindromeRearranging(inputString):

    # BETTER SOLUTION

    # return sum([inputString.count(c) % 2 for c in set(inputString)]) <= 1

    if len(set(inputString)) == 1 or len(inputString) == 1:

        return True

    if len(inputString) == 2:

        return False

    evens = 0
    odds = 0

    char_count = dict()

    for char in inputString:

        if char not in char_count:

            char_count[char] = 0

        char_count[char] += 1

    for k in char_count:

        if char_count[k] % 2 == 0:

            evens += 1

        else:

            odds += 1

    if len(inputString) % 2 == 0:

        print(evens, len(char_count))

        if evens == len(char_count):

            return True

        else:

            return False

    else:

        if evens > odds:

            return True

        elif evens == odds:

            if len(inputString) == 3:

                return True

            else:

                return False

        else:

            return False
