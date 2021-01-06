def knapsackLight(value1, weight1, value2, weight2, maxW):

    if weight1 > maxW and weight2 > maxW:

        return 0

    elif weight1 + weight2 <= maxW:

        return value1 + value2

    else:

        if weight1 < maxW and weight2 < maxW:

            return max(value1, value2)

        else:

            if weight1 > maxW:

                return value2

            elif weight2 > maxW:

                return value1

            else:

                if weight1 == maxW or weight2 == maxW:

                    return max(value1, value2)
