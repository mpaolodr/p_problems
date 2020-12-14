
def isPalindrome(x: int) -> bool:

    if x < 0 or (x % 10 == 0 and x != 0):

        return False

    reverted_number = 0

    while x > reverted_number:

        reverted_number = reverted_number * 10 + x % 10

        x = x // 10

    return x == reverted_number or x == reverted_number // 10
# def isPalindrome(self, x: int) -> bool:

#     if str(x) == str(x)[::-1]:

#         return True


#     return False
print(isPalindrome(12221))
