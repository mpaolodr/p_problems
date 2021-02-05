def goodTuples(a):

    count = 0

    for i in range(len(a) - 2):

        nums = set()

        for j in range(i, i + 3):

            nums.add(a[j])

        if len(nums) == 2:

            count += 1

    return count


a = [1, 1, 1, 2, 1, 3, 4]
b = [1, 1, 2, 1, 2, 1, 1]

print(goodTuples(a))
print(goodTuples(b))
