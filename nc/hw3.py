"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

"""


def csReverseIntegerBits(n):

    to_bin = bin(n)[::-1]

    return int(f"0b{to_bin[:-2]}", 2)
