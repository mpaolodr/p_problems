def arrayMaxConsecutiveSum(inputArray, k):

    if k == len(inputArray):

        return sum(inputArray)

    if k == 1:

        return max(inputArray)

    cur_total = sum(inputArray[:k])
    max_total = cur_total

    for i in range(len(inputArray) - k):

        cur_total = cur_total - inputArray[i] + inputArray[i + k]
        max_total = max(max_total, cur_total)

    return max_total

    # fails one test
    # i = 0

    # total = 0

    # while i < len(inputArray) - (k - 1):

    #     new_sum = sum(inputArray[i: k + i])
    #     total = max(total, new_sum)

    #     i += 1

    # return total
