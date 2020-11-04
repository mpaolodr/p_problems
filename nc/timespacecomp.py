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


# def csFindAddedLetter(str_1, str_2):

#     dict_str_1 = dict()
#     dict_str_2 = dict()

#     for i in range(len(str_1)):

#         if str_1[i] not in dict_str_1:

#             dict_str_1[str_1[i]] = 0

#         dict_str_1[str_1[i]] += 1

#     for i in range(len(str_2)):

#         if str_2[i] not in dict_str_2:

#             dict_str_2[str_2[i]] = 0

#         dict_str_2[str_2[i]] += 1

#     for k in dict_str_2:

#         if k not in dict_str_1 or dict_str_2[k] != dict_str_1[k]:

#             return k


def csFindAddedLetter(str_1, str_2):
    m = len(str_1)
    n = len(str_2)

    j = 0    # Index of str1
    i = 0    # Index of str2

    while j < m and i < n:

        # if there's a mismatch, that's the added string so we return that
        if str_1[j] != str_2[i]:

            return str_2[i]

        # no mismatch, we just increment both pointers (j and i)
        i += 1
        j += 1

    # exits the while loop

    return str_2[i]


print(csFindAddedLetter("bcde", "bcdef"))
print(csFindAddedLetter("", "z"))
print(csFindAddedLetter("b", "bb"))
print(csFindAddedLetter("f", "bfb"))
print(csFindAddedLetter("xqmxtheyvpdqounqmfyaqdqxwe", "xqmxtheyvpdqounqmfyaqxdqxwe"))


def csSortedTwoSum(numbers, target):

    num_dict = dict()

    for i in range(len(numbers)):

        if numbers[i] not in num_dict:

            num_dict[numbers[i]] = list()

        num_dict[numbers[i]].append(i)

    for k in num_dict:

        needed = target - k

        if needed in num_dict:

            if len(num_dict[needed]) > 1:

                return [num_dict[needed][0], num_dict[needed][1]]

            else:

                return [min(num_dict[needed][0], num_dict[k][0]), max(num_dict[needed][0], num_dict[k][0])]
