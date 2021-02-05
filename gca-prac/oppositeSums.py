"""


Consider a function rev which reverses the digits in an integer. Here are some examples:

rev(103) = 301
rev(2400) = 42
rev(9) = 9

Given an array of non-negative integers arr, 
your task is to count the number of pairs (i, j) 

such that i ≤ j and arr[i] + rev(arr[j]) = arr[j] + rev(arr[i]).

Example
For arr = [1, 20, 2, 11], the output should be oppositeSums(arr) = 7.
For (i, j) = (0, 0) equality holds: 1 + 1 = 1 + 1,
For (i, j) = (0, 1) equality doesn't hold: 1 + 2 ≠ 20 + 1,
For (i, j) = (0, 2) equality holds: 1 + 2 = 2 + 1,
For (i, j) = (0, 3) equality holds: 1 + 11 = 11 + 1,
For (i, j) = (1, 1) equality holds: 20 + 2 = 20 + 2,
For (i, j) = (1, 2) equality doesn't hold: 20 + 2 ≠ 2 + 2,
For (i, j) = (1, 3) equality doesn't hold: 20 + 11 ≠ 11 + 2,
For (i, j) = (2, 2) equality holds: 2 + 2 = 2 + 2,
For (i, j) = (2, 3) equality holds: 2 + 11 = 11 + 2,
For (i, j) = (3, 3) equality holds: 11 + 11 = 11 + 11,

"""


def oppositeSums(arr):

    count = 0

    for i in range(len(arr)):

        for j in range(i, len(arr)):

            first_condition = arr[i] + reverser(arr[j])
            second_condition = arr[j] + reverser(arr[i])

            if first_condition == second_condition:

                count += 1

    return count


def reverser(n):

    rev_num = int(str(n)[::-1])

    return rev_num


arr = [1, 20, 2, 11]
arr1 = [32, 332, 100]

print(oppositeSums(arr))
print(oppositeSums(arr1))
