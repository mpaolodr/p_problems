def primeChecker(num):

    nums = list()

    for n in range(2, num + 1):

        nums.append(n)

    bool_nums = [False for num in nums]

    i = 0

    while i < len(bool_nums):

        if not bool_nums[i]:

            cur_num = nums[i]

            j = i + 1

            while j < len(nums):

                if nums[j] % cur_num == 0 and cur_num ** 2 <= nums[j]:

                    bool_nums[j] = True

                j += 1

        i += 1

    primes = list()

    for i in range(len(bool_nums)):

        if not bool_nums[i]:

            primes.append(nums[i])

    return primes
