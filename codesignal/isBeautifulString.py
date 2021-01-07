def isBeautifulString(inputString):

    char_count = dict()

    for char in inputString:

        if char not in char_count:

            char_count[char] = 0

        char_count[char] += 1

    for num in range(97, 123):

        if chr(num) not in char_count:

            char_count[chr(num)] = 0

    for key in char_count:

        if ord(key) > 97 and ord(key) < 123:

            if char_count[key] > char_count[chr(ord(key) - 1)]:

                return False

    return True
