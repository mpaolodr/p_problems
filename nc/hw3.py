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
