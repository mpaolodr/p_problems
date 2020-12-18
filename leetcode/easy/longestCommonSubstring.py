class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:

            return ""

        if len(strs[0]) == 0:

            return ""

        i = 0

        while True:

            prefix = strs[0][0: i + 1]

            if i == len(strs[0]):

                return prefix

            for word in strs:

                if word[:len(prefix)] != prefix:

                    return prefix[:-1]

            i += 1
