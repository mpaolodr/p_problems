"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""


def two_sum(nums, target):
    # Your code here

    elem_indices = dict()

    for i in range(len(nums)):

        if nums[i] not in elem_indices:

            elem_indices[nums[i]] = list()

        elem_indices[nums[i]].append(i)

    for key in elem_indices:

        needed = target - key

        if needed in nums:

            # in case there are duplicates
            if needed != key:

                return [elem_indices[needed][0], elem_indices[key][0]]

            else:

                # if there are duplicates, we return the first 2,
                # if key is the ssame as needed and it only has length of 1, we do nothing
                if len(elem_indices[needed]) > 1:

                    return [elem_indices[needed][0], elem_indices[needed][1]]

    return elem_indices


print(two_sum([2, 5, 9, 13], 7))
print(two_sum([4, 3, 5], 8))


"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""


def single_number(nums):
    # Your code here

    res = 0

    for num in nums:

        res ^= num

    return res


print(single_number([3, 3, 2]))
print(single_number([5, 2, 3, 2, 3]))
print(single_number([10]))
