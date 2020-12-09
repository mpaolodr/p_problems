class Solution:
    def myAtoi(self, s: str) -> int:

        clear_whitespace = s.strip(" ")

        if len(s) == 0 or len(clear_whitespace) == 0:

            return 0

        if not clear_whitespace[0].isnumeric():

            if clear_whitespace[0] != "-" and clear_whitespace[0] != "+":

                return 0

        to_convert = ""

        for i in range(len(clear_whitespace)):

            if i == 0:

                if clear_whitespace[i] == "-" or clear_whitespace[i] == "+":

                    to_convert += clear_whitespace[i]

                else:

                    if clear_whitespace[i].isnumeric():

                        to_convert += clear_whitespace[i]

                    else:

                        break

            else:

                if clear_whitespace[i].isnumeric():

                    to_convert += clear_whitespace[i]

                else:

                    break

        if to_convert == "-" or to_convert == "+":

            return 0

        if int(to_convert) < -2 ** 31:

            return -2 ** 31

        elif int(to_convert) > (2 ** 31) - 1:

            return (2 ** 31) - 1

        else:

            return int(to_convert)
