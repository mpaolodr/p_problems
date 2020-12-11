class Solution:
    def romanToInt(self, s: str) -> int:

        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0

        i = len(s) - 1

        while i > -1:

            if i - 1 >= 0:

                if values[s[i]] > values[s[i - 1]]:

                    total += values[s[i]] - values[s[i - 1]]
                    i -= 2

                else:

                    total += values[s[i]]
                    i -= 1

            else:

                total += values[s[i]]
                i -= 1

        return total
