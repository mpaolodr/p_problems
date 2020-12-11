class Solution:
    def intToRoman(self, num: int) -> str:

        result = ""

        while num > 10:

            result += self.convert(num)

            if num > 999:

                num = num % 1000

            elif num > 99:

                num = num % 100

            elif num > 9:

                num = num % 10

        result += self.convert(num)
        return result

    def convert(self, num):

        values = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I"
        }

        if num > 999:

            number_of_m = num // 1000

            return values[1000] * number_of_m

        if num > 99:

            number_of_c = num // 100

            if number_of_c > 8:

                return values[100] + values[1000]

            else:

                if number_of_c > 5:

                    return values[500] + ((number_of_c - 5) * values[100])

                else:

                    if number_of_c == 5:

                        return values[500]

                    elif number_of_c == 4:

                        return values[100] + values[500]

                    else:

                        return values[100] * number_of_c

        if num > 9:

            number_of_x = num // 10

            if number_of_x > 8:

                return values[10] + values[100]

            else:

                if number_of_x > 5:

                    return values[50] + ((number_of_x - 5) * values[10])

                else:

                    if number_of_x == 5:

                        return values[50]

                    elif number_of_x == 4:

                        return values[10] + values[50]

                    else:

                        return values[10] * number_of_x

        if num < 10:

            if num == 9:

                return values[1] + values[10]

            else:

                if num > 5:

                    return values[5] + ((num - 5) * values[1])

                else:

                    if num == 5:

                        return values[5]

                    elif num == 4:

                        return values[1] + values[5]

                    else:

                        return values[1] * num
