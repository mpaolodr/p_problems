class Solution:
    def toLowerCase(self, str: str) -> str:

        to_list = list(str)

        for i, char in enumerate(to_list):

            if 65 <= ord(char) <= 90:

                to_list[i] = chr(ord(char) + 32)

        return "".join(to_list)
