class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1 or s == s[::-1]:

            return s

        if len(set(s)) == len(s) or len(set(s)) == 1:

            return s[0]

        current_longest = ""

        i = 0

        while i < len(s) - 1:

            j = len(s) - 1

            while j >= i:

                if s[i] == s[j]:

                    current_string = s[i:j + 1]
                    reversed_string = current_string[::-1]

                    if reversed_string == current_string and len(reversed_string) > len(current_longest):

                        current_longest = reversed_string

                j -= 1

            i += 1

        return current_longest
