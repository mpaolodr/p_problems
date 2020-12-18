class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # two pointer approach

        sorted_nums = sorted(nums)
        results = list()

        seen = set()

        for i in range(len(sorted_nums)):

            lo = i + 1
            hi = len(sorted_nums) - 1

            while lo < hi:

                sum_vals = sorted_nums[i] + sorted_nums[lo] + sorted_nums[hi]

                if sum_vals < 0:

                    lo += 1

                elif sum_vals > 0:

                    hi -= 1

                else:

                    if (sorted_nums[i], sorted_nums[lo], sorted_nums[hi]) not in seen:

                        seen.add(
                            (sorted_nums[i], sorted_nums[lo], sorted_nums[hi]))

                        results.append(
                            [sorted_nums[i], sorted_nums[lo], sorted_nums[hi]])

                    lo += 1
                    hi -= 1

        return results

        # if len(nums) < 3:

        #     return []

        # sum_dict = dict()
        # count_dict = dict()

        # for i in range(len(nums)):

        #     if nums[i] not in count_dict:

        #         count_dict[nums[i]] = 0

        #     count_dict[nums[i]] += 1

        #     for j in range(len(nums)):

        #         if ((nums[i], nums[j]) not in sum_dict) and (nums[j], nums[i]) not in sum_dict:

        #             sum_dict[nums[i], nums[j]] = (nums[i] + nums[j]) * -1

        # tracker = set()
        # pos_results = list()

        # checker = set(nums)

        # for k in sum_dict:

        #     if sum_dict[k] in checker and tuple(sorted([sum_dict[k], k[0], k[1]])) not in tracker:

        #         if sum_dict[k] == k[0] and sum_dict[k] == k[1]:

        #             if count_dict[sum_dict[k]] > 2:

        #                 pos_results.append([sum_dict[k], k[0], k[1]])

        #         elif sum_dict[k] == k[0] or sum_dict[k] == k[1]:

        #             if count_dict[sum_dict[k]] > 1:

        #                 pos_results.append([sum_dict[k], k[0], k[1]])

        #         elif k[0] == k[1]:

        #             if count_dict[k[0]] >= 2:

        #                 pos_results.append([sum_dict[k], k[0], k[1]])

        #         else:

        #             pos_results.append([sum_dict[k], k[0], k[1]])

        #         tracker.add(tuple(sorted([sum_dict[k], k[0], k[1]])))

        # return pos_results


"""
sorted_nums = sorted(nums)
        results = list()
        
        tracker = set()
        
        
        count_dict = dict()
        
        for num in nums:
            
            if num not in count_dict:
                
                count_dict[num] = 0
                
            count_dict[num] += 1
    
        for i in range(len(sorted_nums)):
            
            target = -sorted_nums[i]
            
            s = i
            e = len(sorted_nums) - 1
            
            while s < e:
                
                two_sum = sorted_nums[s] + sorted_nums[e]
                
                if target > two_sum:
                    
                    s += 1
                    
                elif target < two_sum:
                    
                    e -= 1
                    
                else:
                    
                    if (sorted_nums[s], sorted_nums[e], sorted_nums[i]) not in tracker:
                        
                        tracker.add((sorted_nums[s], sorted_nums[e], sorted_nums[i]))
                        
                        if sorted_nums[s] == sorted_nums[e] and sorted_nums[e] == sorted_nums[i]:
                            
                            if count_dict[sorted_nums[s]] > 2:
                                
                                results.append([sorted_nums[s], sorted_nums[e], sorted_nums[i]])
                                 
                        elif sorted_nums[s] == sorted_nums[i] or sorted_nums[i] == sorted_nums[e]:
                            
                            if count_dict[sorted_nums[s]] > 1 or count_dict[sorted_nums[e]] > 1:
                                
                                results.append([sorted_nums[s], sorted_nums[e], sorted_nums[i]])
                        
                        elif sorted_nums[s] == sorted_nums[e]:
                            
                            if count_dict[sorted_nums[e]] >= 2:
                                
                                results.append([sorted_nums[s], sorted_nums[e], sorted_nums[i]])
                        
                        else:
                            
                            results.append([sorted_nums[s], sorted_nums[e], sorted_nums[i]])
                    
                    
                    s += 1
                    e -= 1
                    
                    
        return results

fails due to duplicates
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # 3sum probs can be solved with two pointer approach

        diff = 2**31 - 1

        sorted_nums = sorted(nums)

        i = 0

        while i < len(sorted_nums):

            if diff == 0:

                break

            lo = i + 1
            hi = len(sorted_nums) - 1

            while lo < hi:

                sum_values = sorted_nums[i] + sorted_nums[lo] + sorted_nums[hi]

                if abs(target - sum_values) < abs(diff):

                    diff = target - sum_values

                if sum_values < target:

                    lo += 1

                else:

                    hi -= 1

            i += 1

        return target - diff
