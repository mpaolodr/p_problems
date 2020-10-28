def removeEvens(numbers):

    for i in reversed(range(len(numbers))):

        if numbers[i] % 2 == 0:

            del numbers[i]

    return numbers
