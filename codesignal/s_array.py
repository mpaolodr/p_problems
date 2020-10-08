def csSearchRotatedSortedArray(nums, target):

    pivot = find_pivot(nums)

    pivoted_start = pivot
    pivoted_end = pivot - 1

    # check if start or end is already the target
    if nums[pivoted_start] == target:

        return pivoted_start

    if nums[pivoted_end] == target:

        return pivoted_end

    before_pivot_start = 0
    before_pivot_end = pivot - 1

    pivoted_start = pivot
    pivoted_end = len(nums) - 1

    if target < nums[before_pivot_start]:

        return search(nums, target, pivoted_start, pivoted_end)

    else:

        return search(nums, target, before_pivot_start, before_pivot_end)


def search(nums, target, start, end):

    low = start
    high = end

    while low <= high:

        mid = (low + high) // 2

        if target == nums[mid]:

            return mid

        else:

            if target > nums[mid]:

                low = mid + 1

            else:

                high = mid - 1

    return -1


def find_pivot(nums):

    start = 0
    end = len(nums) - 1

    if nums[start] < nums[end]:

        return 0

    while end - start > 2:

        mid = (start + end) // 2

        if nums[mid] > nums[end]:

            start = mid

        # nums[mid] < nums[end]
        else:

            end = mid

    current_mid = end - 1

    if nums[current_mid] < nums[end] and nums[current_mid] < nums[start]:

        return current_mid

    else:

        return end
