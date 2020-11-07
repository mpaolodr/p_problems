def allLongestStrings(inputArray):

    max_len = max([len(el) for el in inputArray])

    results = list()

    for item in inputArray:

        if len(item) == max_len:

            results.append(item)

    return results
