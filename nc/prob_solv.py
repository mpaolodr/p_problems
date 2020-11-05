# def csRemoveTheVowels(input_str):

#     vowels = {"a", "e", "i", "o", "u", "A", "I", "E", "O", "U"}

#     input_copy = input_str.lower()

#     for x in input_str:

#         print(input_copy)

#         if x in vowels:

#             input_copy = input_copy.replace(x, "")

#     return input_copy


# print(csRemoveTheVowels(
#     "f!a fbs,rI\\H[P^f}!h;!<\tyu>/`uD^d,xGDWPj{HU$m~$|_e#"))
# print(csRemoveTheVowels("aabcde"))
# print(csRemoveTheVowels("aaaaaaeeeeeeb"))


def csRemoveTheVowels(input_str):

    vowels = {"a", "e", "i", "o", "u", "A", "I", "E", "O", "U"}

    input_copy = input_str

    for i in range(len(input_str) - 1, 0, -1):

        if input_str[i] in vowels:

            input_copy = input_copy[:i] + input_copy[i + 1:]

    return input_copy


def csShortestWord(input_str):

    string_split = input_str.split()

    shortest_word = len(string_split[0])

    for word in string_split:

        if len(word) < shortest_word:

            shortest_word = len(word)

    return shortest_word


def csSumOfPositive(input_arr):

    sum_of_pos = 0

    for num in input_arr:

        if num > 0:

            sum_of_pos += num

    return sum_of_pos


def csLongestPossible(str_1, str_2):

    combined = set(str_1).union(set(str_2))

    result = "".join(sorted(list(combined)))

    return result


def csAnythingButFive(start, end):

    count = 0

    for num in range(start, end + 1):

        num_check = check_five(num)

        if num_check == False:

            count += 1

    return count


def check_five(n):

    to_string = str(n)

    for char in to_string:

        if char == "5":

            return True

    return False
