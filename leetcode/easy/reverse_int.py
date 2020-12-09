class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        digits = reversed(list(str(x)))
        reversed_list = []

        for char in digits:

            if char.isdigit():

                reversed_list.append(char)

            else:

                reversed_list.insert(0, char)

        reversed_digits = int("".join(reversed_list))

        if reversed_digits >= (-2 ** 31) and reversed_digits <= ((2 ** 31) - 1):

            return reversed_digits

        else:

            return 0
