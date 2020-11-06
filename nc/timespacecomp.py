# def csFirstUniqueChar(input_str):

#     if len(set(input_str)) == 1 or len(input_str) == 0:

#         return -1

#     char_dict = dict()

#     for i in range(len(input_str)):

#         if input_str[i] not in char_dict:

#             char_dict[input_str[i]] = 0

#         char_dict[input_str[i]] += 1

#     for c in range(len(input_str)):

#         if char_dict[input_str[c]] == 1:

#             return c

#     else:

#         return -1


def csFirstUniqueChar(input_str):
    '''
    '''

    none = int(-1)

    if len(input_str) == 0:

        return none

    else:

        chars = list(input_str)
        char_dict = dict()

        for c in chars:

            if c not in char_dict:

                char_dict[c] = 0

            char_dict[c] += 1

        for i, c in enumerate(input_str):

            if char_dict[c] == 1:

                return i

        else:

            return -1


print(csFirstUniqueChar("abc"))  # a - 0
print(csFirstUniqueChar("aaaaabc"))  # b - 5
print(csFirstUniqueChar("aaa"))  # -1
print(csFirstUniqueChar("aabbc"))  # c - 4


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

    result = [char for char in set(
        str_2) if str_1.count(char) != str_2.count(char)][0]

    return result


print(csFindAddedLetter("bcde", "bcdef"), "TEST 1")
print(csFindAddedLetter("", "z"), "TEST 2")
print(csFindAddedLetter("b", "bb"), "TEST 3")
print(csFindAddedLetter("bf", "bfb"), "TEST 4")
print(csFindAddedLetter("xqmxtheyvpdqounqmfyaqdqxwe",
                        "xqmxtheyvpdqounqmfyaqxdqxwe"), "TEST 5")
print(csFindAddedLetter("abcd", "dcbae"), "TEST 6")


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
