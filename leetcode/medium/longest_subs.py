class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:

            return 0

        if len(set(s)) == len(s):

            return len(s)

        elif len(set(s)) == 1:

            return 1

        possible_results = list()

        for i in range(len(s)):

            sub_s = {s[i]}

            for j in range(i + 1, len(s)):

                if s[j] in sub_s:

                    break

                else:

                    sub_s.add(s[j])

            possible_results.append(len(sub_s))

        return max(possible_results)
