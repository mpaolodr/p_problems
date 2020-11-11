def csFindTheSingleNumber(nums):

    # first solution
    count_dict = dict()

    for n in nums:

        if n not in count_dict:

            count_dict[n] = 0

        count_dict[n] += 1

    for k in count_dict:

        if count_dict[k] == 1:

            return k
