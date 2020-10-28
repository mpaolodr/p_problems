from typing import List
import string


def removeEvens(numbers):

    for i in reversed(range(len(numbers))):

        if numbers[i] % 2 == 0:

            del numbers[i]

    return numbers


def arrayMedian(sequence):

    # sort in place - mutating the input
    sequence.sort()

    if len(sequence) % 2 == 0:

        return even_median(sequence)

    else:

        return odd_median(sequence)


def odd_median(arr):

    mid = len(arr) // 2

    return arr[mid]


def even_median(arr):

    mid1 = len(arr) // 2
    mid2 = mid1 - 1

    return (arr[mid1] + arr[mid2]) / 2


def increasingSubstrings(s):

    letters = list(string.ascii_letters)

    results = list()
    pointer = 0

    for i in range(len(s)):

        if i < len(s) - 1:

            next_in_letters = letters[letters.index(s[i + 1]) - 1]

            if next_in_letters != s[i]:

                results.append(s[pointer: i + 1])
                pointer = i + 1

        else:

            results.append(s[pointer: i + 1])

    return results


# sol code


# def char_is_next(a: str, b: str) -> bool:
#     return ord(a) + 1 == ord(b)


# def increasingSubstrings(s: str) -> List[str]:
#     if len(s) == 1:
#         return [s]

#     output = []
#     a, b = 0, 1

#     while b < len(s):
#         if not char_is_next(s[b - 1], s[b]):
#             output.append(s[a:b])
#             a = b

#         if b + 1 == len(s):
#             output.append(s[a:b + 1])
#             break

#         b += 1

#     return output
