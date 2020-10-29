"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

"""


def csReverseIntegerBits(n):

    to_bin = bin(n)[::-1]

    return int(f"0b{to_bin[:-2]}", 2)


"""
Given an array of positive integers a, your task is to calculate how many of its elements have an even number of digits.

Example

For a = [12, 134, 111, 1111, 10], the output should be evenDigitsNumber(a) = 3.

a[0] = 12 has 2 digits, which is an even number.
a[1] = 134 has 3 digits, which is not an even number.
a[2] = 111 has 3 digits, which is not an even number.
a[3] = 1111 has 4 digits, which is an even number.
a[4] = 10 has 2 digits, which is an even number.
There are 3 elements (a[0], a[3], and a[4]) with an even number of digits, so the answer is 3.


"""


def evenDigitsNumber(a):

    even_count = 0

    for num in a:

        if count_digits(num) % 2 == 0:

            even_count += 1

    return even_count


def count_digits(n, count=0):

    if n < 10:

        count += 1
        return count

    count += 1
    return count_digits(n // 10, count)


"""
You're writing a new programming language and you'd like it to have the capability of splitting a string into substrings with limited characters. More specifically, we'll call a substring good if the absolute difference in ASCII codes between any two of its characters is less than or equal to k.

For example, if k = 3, then the string "bad" would be considered good, since the greatest difference in ASCII codes is 3 (between the a and d characters). The string "nice" would not be considered good, since there's a difference of 11 between the c and n characters.

You are given a string strToSplit that consists of lowercase English letters only, and your task is to find the minimal number of good substrings you can split it into.

Hint: Iterate over the string strToSplit and keep the ASCII codes of the smallest and the greatest characters in the current substring. Every time when the difference between them becomes greater than k, it means that the last considered symbol should be the first one in a new substring.

Example

For strToSplit = "aaabaaabb" and k = 0, the output should be goodSubstrings(strToSplit, k) = 4.

strToSplit could be split into ["aaa", "b", "aaa", "bb"]. Each substring must consist of only one type of character, because it is required that |s[i] - s[j]| ≤ 0 for each substring s.

For strToSplit = "aaabaaabb" and k = 1, the output should be goodSubstrings(strToSplit, k) = 1.

Since the only characters in the string have a difference of 1, aaabaaabb meets the requirement |strToSplit[i] - strToSplit[j]| ≤ 1. So only 1 substring is required (and it's the full original string).

For strToSplit = "aaabzaaabb" and k = 10, the output should be goodSubstrings(strToSplit, k) = 3.

strToSplit could be split into ["aaab", "z", "aaabb"]. Since the z character has such a large difference with each of its adjacent characters, it must be in a substring of its own.

"""


def goodSubstrings(strToSplit, k):

    if len(strToSplit) == 1 or len(set(strToSplit)) == 1:

        return 1

    results = list()

    sub_s = strToSplit[0]

    max_code_in_sub_s = ord(strToSplit[0])
    min_code_in_sub_s = ord(strToSplit[0])

    for i in range(1, len(strToSplit)):

        for char in sub_s:

            if ord(char) > max_code_in_sub_s:

                max_code_in_sub_s = ord(char)

            if ord(char) < min_code_in_sub_s:

                min_code_in_sub_s = ord(char)

        if abs(max_code_in_sub_s - ord(strToSplit[i])) <= k and abs(min_code_in_sub_s - ord(strToSplit[i])) <= k:

            sub_s += strToSplit[i]

        else:

            results.append(sub_s)
            sub_s = strToSplit[i]
            max_code_in_sub_s = ord(strToSplit[i])
            min_code_in_sub_s = ord(strToSplit[i])

    results.append(sub_s)

    return len(results)
