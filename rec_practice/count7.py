"""
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


count7(717) → 2
count7(7) → 1
count7(123) → 0

"""


def count7(n):

    if n < 10:

        if n == 7:

            return 1

        else:

            return 0

    else:

        num = count7(n // 10)

        if n % 10 == 7:

            return 1 + num

        else:

            return num


def count7(n):

    if type(n) == int:

        str_n = str(n)

    else:

        str_n = n

    if len(str_n) == 1:

        if str_n == "7":

            return 1

        else:

            return 0

    else:

        test = str_n[0]

        if test == "7":

            return 1 + count7(str_n[1:])

        else:

            return count7(str_n[1:])


print(count7(710077))
print(count7(1234567890))
print(count7(123))
