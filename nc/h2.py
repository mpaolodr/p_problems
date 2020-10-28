def removeEvens(numbers):

    for i in reversed(range(len(numbers))):

        if numbers[i] % 2 == 0:

            del numbers[i]

    return numbers


def arrayMedian(sequence):

    # sort in place - mutating the input
    sequence.sort()

    if len(sequence) % 2 == 0:

        return even_median(sequence)

    else:

        return odd_median(sequence)


def odd_median(arr):

    mid = len(arr) // 2

    return arr[mid]


def even_median(arr):

    mid1 = len(arr) // 2
    mid2 = mid1 - 1

    return (arr[mid1] + arr[mid2]) / 2
