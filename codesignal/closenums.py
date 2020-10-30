def containsCloseNums(nums, k):

    position = dict()

    for i in range(len(nums)):

        if nums[i] not in position:

            position[nums[i]] = list()

        position[nums[i]].append(i)

    for key in position:

        if len(position[key]) == 2:

            if abs(position[key][0] - position[key][1]) <= k:

                return True

        elif len(position[key]) > 2:

            for i in range(len(position[key])):

                for j in range(i + 1, len(position[key])):

                    if abs(position[key][i] - position[key][j]) <= k:

                        return True

    return False
