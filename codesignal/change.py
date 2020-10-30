def arrayChange(inputArray):

    count = 0
    prev = inputArray[0]

    for i in range(1, len(inputArray)):

        if inputArray[i] < prev:

            prev_value = inputArray[i]
            inputArray[i] = inputArray[i] + ((prev - inputArray[i]) + 1)
            count += inputArray[i] - prev_value

        elif inputArray[i] == prev:

            inputArray[i] = inputArray[i] + 1
            count += 1

        prev = inputArray[i]

    return count
