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


print(count7(710077))
print(count7(1234567890))
print(count7(123))
