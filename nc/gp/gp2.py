"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
    # Your code here

    if n > len(a):

        return "Invalid"

    if n == 0:

        return list()

    return a[len(a) - n:]


list1 = [1, 2, 3, 4, 5]
list2 = [4, 3, 9, 9, 7, 6]


print(last(list1, 1))
print(last(list2, 3))
print(last(list1, 7))
print(last(list1, 0))
print(last(list1, 3))
