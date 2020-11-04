def csFirstUniqueChar(input_str):

    if len(set(input_str)) == 1 or len(input_str) == 0:

        return -1

    char_dict = dict()

    for i in range(len(input_str)):

        if input_str[i] not in char_dict:

            char_dict[input_str[i]] = 0

        char_dict[input_str[i]] += 1

    for c in range(len(input_str)):

        if char_dict[input_str[c]] == 1:

            return c

    else:

        return -1
