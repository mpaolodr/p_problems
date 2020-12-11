"""
Solution failing: Needs to be optimized

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # index_dict = {i: 0 for i in range(len(height) - 1)}

        # for k in index_dict:

        #     for j in range(k + 1, len(height)):

        #         index_dict[k] = max(index_dict[k], self.volume(k, j, height))

        # return max(index_dict.values())

        max_area = 0

        start = 0
        end = len(height) - 1

        while start < end:

            max_area = max(self.volume(start, end, height), max_area)

            if height[start] > height[end]:

                end -= 1

            else:

                start += 1

        return max_area

    def volume(self, start, end, arr):

        index_diff = end - start
        minimum = min(arr[start], arr[end])

        return index_diff * minimum
