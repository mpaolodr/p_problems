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


def csFindAddedLetter(str_1, str_2):

    dict_str_1 = dict()
    dict_str_2 = dict()

    for i in range(len(str_1)):

        if str_1[i] not in dict_str_1:

            dict_str_1[str_1[i]] = 0

        dict_str_1[str_1[i]] += 1

    for i in range(len(str_2)):

        if str_2[i] not in dict_str_2:

            dict_str_2[str_2[i]] = 0

        dict_str_2[str_2[i]] += 1

    for k in dict_str_2:

        if k not in dict_str_1 or dict_str_2[k] != dict_str_1[k]:

            return k
