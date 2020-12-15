def extractEachKth(inputArray, k):

    # counter = 0

    # for i in range(len(inputArray)):

    #     if counter == k - 1:

    #         inputArray[i] = None
    #         counter = 0

    #     else:

    #         counter += 1

    # i = 0

    # while i < len(inputArray):

    #     if inputArray[i] == None:

    #         del inputArray[i]
    #         i = i

    #     else:

    #         i += 1

    # return inputArray

    # different solution

    # del inputArray[k - 1::k]

    # return inputArray

    # list comprehension
    return [i for (n, index) in range(len(inputArray)) if (index + 1) % k == 0]
