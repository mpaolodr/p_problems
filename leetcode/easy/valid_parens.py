class Solution:
    def isValid(self, s: str) -> bool:

        seen = list()

        opening = {"(": ")", "{": "}", "[": "]"}

        for char in s:

            if char in opening:

                seen.append(char)

            else:

                if len(seen) == 0:

                    return False

                opening_pair = seen.pop()

                if opening[opening_pair] != char:

                    return False

        return len(seen) == 0
