class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:

            return []

        sum_dict = dict()
        count_dict = dict()

        for i in range(len(nums)):

            if nums[i] not in count_dict:

                count_dict[nums[i]] = 0

            count_dict[nums[i]] += 1

            for j in range(len(nums)):

                if ((nums[i], nums[j]) not in sum_dict) and (nums[j], nums[i]) not in sum_dict:

                    sum_dict[nums[i], nums[j]] = (nums[i] + nums[j]) * -1

        tracker = set()
        pos_results = list()

        checker = set(nums)

        for k in sum_dict:

            if sum_dict[k] in checker and tuple(sorted([sum_dict[k], k[0], k[1]])) not in tracker:

                if sum_dict[k] == k[0] and sum_dict[k] == k[1]:

                    if count_dict[sum_dict[k]] > 2:

                        pos_results.append([sum_dict[k], k[0], k[1]])

                elif sum_dict[k] == k[0] or sum_dict[k] == k[1]:

                    if count_dict[sum_dict[k]] > 1:

                        pos_results.append([sum_dict[k], k[0], k[1]])

                elif k[0] == k[1]:

                    if count_dict[k[0]] >= 2:

                        pos_results.append([sum_dict[k], k[0], k[1]])

                else:

                    pos_results.append([sum_dict[k], k[0], k[1]])

                tracker.add(tuple(sorted([sum_dict[k], k[0], k[1]])))

        return pos_results
