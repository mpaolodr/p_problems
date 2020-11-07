def matrixElementsSum(matrix):

    ind_list_length = len(matrix[0])
    total = 0

    j = 0

    while j < ind_list_length:

        i = 0

        while i < len(matrix):

            if matrix[i][j] == 0:
                break
            else:

                total += matrix[i][j]
                i += 1

        j += 1

    return total
