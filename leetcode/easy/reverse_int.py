class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        rev = 0

        while x != 0:

            pop = x % 10
            x //= 10

            if rev > (2**31 - 1 // 10) or (rev == 2**31 - 1 // 10 and pop > 7):

                return 0

            if rev < (-2**31 // 10) or (rev == -2**31 // 10 and pop <= -8):

                return 0

            rev = rev * 10 + pop

        return rev


x = Solution()

print(x.reverse(-122))

# def reverse(self, x):
#     """
#     :type x: int
#     :rtype: int
#     """

#     digits = reversed(list(str(x)))
#     reversed_list = []

#     for char in digits:

#         if char.isdigit():

#             reversed_list.append(char)

#         else:

#             reversed_list.insert(0, char)

#     reversed_digits = int("".join(reversed_list))

#     if reversed_digits >= (-2 ** 31) and reversed_digits <= ((2 ** 31) - 1):

#         return reversed_digits

#     else:

#         return 0
