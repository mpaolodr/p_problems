"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""

import math


def plus_one(d):
    # Your code here

    # first pass

    # sum_to_arr = int("".join([str(d) for d in digits])) + 1
    # result = [int(n) for n in str(sum_to_arr)]

    # return result

    if d[-1] < 9:

        d[-1] += 1

        return d

    # this will run if last digit is 9

    # we keep track of the last index that was 9
    last_9 = len(d) - 1

    # we mutate the array in-place
    d[-1] = 0

    for i in range(len(d) - 1, -1, -1):

        if last_9 - i == 1:

            if d[i] == 9:

                last_9 = i
                d[i] = 0

            else:

                d[i] += 1
                break

    if last_9 == 0:

        d.insert(0, 1)

    return d


    # return digits
print(plus_one([1, 3, 2]))  # 133
print(plus_one([3, 2, 1, 9]))  # 3220
print(plus_one([9, 9, 9]))  # 1000
print(plus_one([1, 9, 0]))  # 191
print(plus_one([1, 9, 9, 9]))  # 2000
print(plus_one([1, 1, 9, 9]))  # 1200
