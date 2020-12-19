class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapper = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def comb_builder(combs, next_digits):

            if len(next_digits) == 0:

                output.append(combs)

            else:

                for letter in mapper[next_digits[0]]:

                    comb_builder(combs + letter, next_digits[1:])

        output = list()

        if digits:

            comb_builder("", digits)

        return output
