def minesweeper(matrix):

    result = generate(matrix)

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if i == 0:

                num_bombs = getNbr_first(matrix, i, j)

                result[i][j] = num_bombs

            elif i == len(matrix) - 1:

                num_bombs = getNbr_last(matrix, i, j)

                result[i][j] = num_bombs

            else:

                num_bombs = getNbr_normal(matrix, i, j)

                result[i][j] = num_bombs

    return result


# helpers
def generate(arr):

    result = list()

    for row in arr:

        temp = list()

        for b in row:

            temp.append(0)

        result.append(temp)

    return result


# when i is 0
def getNbr_first(arr, i, j):

    num_bombs = 0

    if j == 0:

        nbr1 = arr[i + 1][j]
        nbr2 = arr[i + 1][j + 1]
        nbr3 = arr[i][j + 1]

        # nbrs = [nbr1, nbr2, nbr3]

        # num_bombs += nbrs.count(True)

        # Makes it look really bad but makes me avoid using any O(n) algorithms
        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

    elif j == len(arr[i]) - 1:

        nbr1 = arr[i + 1][j]
        nbr2 = arr[i + 1][j - 1]
        nbr3 = arr[i][j - 1]

        # nbrs = [nbr1, nbr2, nbr3]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

    else:

        nbr1 = arr[i][j - 1]
        nbr2 = arr[i][j + 1]
        nbr3 = arr[i + 1][j - 1]
        nbr4 = arr[i + 1][j]
        nbr5 = arr[i + 1][j + 1]

        # nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

        if nbr4:

            num_bombs += 1

        if nbr5:

            num_bombs += 1

    return num_bombs

# when i is len(matrix) - 1


def getNbr_last(arr, i, j):

    num_bombs = 0

    if j == 0:

        nbr1 = arr[i - 1][j]
        nbr2 = arr[i - 1][j + 1]
        nbr3 = arr[i][j + 1]

        # nbrs = [nbr1, nbr2, nbr3]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

    elif j == len(arr[i]) - 1:

        nbr1 = arr[i - 1][j]
        nbr2 = arr[i - 1][j - 1]
        nbr3 = arr[i][j - 1]

        # nbrs = [nbr1, nbr2, nbr3]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

    else:

        nbr1 = arr[i][j - 1]
        nbr2 = arr[i][j + 1]
        nbr3 = arr[i - 1][j - 1]
        nbr4 = arr[i - 1][j]
        nbr5 = arr[i - 1][j + 1]

        # nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

        if nbr4:

            num_bombs += 1

        if nbr5:

            num_bombs += 1

    return num_bombs

# if i is not 0 or i not the last element


def getNbr_normal(arr, i, j):

    num_bombs = 0

    if j == 0:

        # top
        nbr1 = arr[i - 1][j]
        nbr2 = arr[i - 1][j + 1]

        # mid
        nbr3 = arr[i][j + 1]

        # bot
        nbr4 = arr[i + 1][j]
        nbr5 = arr[i + 1][j + 1]

        # nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

        if nbr4:

            num_bombs += 1

        if nbr5:

            num_bombs += 1

    elif j == len(arr[i]) - 1:

        # top
        nbr1 = arr[i - 1][j]
        nbr2 = arr[i - 1][j - 1]

        # mid
        nbr3 = arr[i][j - 1]

        # bot
        nbr4 = arr[i + 1][j - 1]
        nbr5 = arr[i + 1][j]

        # nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

        if nbr4:

            num_bombs += 1

        if nbr5:

            num_bombs += 1

    else:

        # top
        nbr1 = arr[i - 1][j - 1]
        nbr2 = arr[i - 1][j]
        nbr3 = arr[i - 1][j + 1]

        # mid
        nbr4 = arr[i][j - 1]
        nbr5 = arr[i][j + 1]

        # bot
        nbr6 = arr[i + 1][j - 1]
        nbr7 = arr[i + 1][j]
        nbr8 = arr[i + 1][j + 1]

        # nbrs = [nbr1, nbr2, nbr3, nbr4, nbr5, nbr6, nbr7, nbr8]

        # num_bombs += nbrs.count(True)

        if nbr1:

            num_bombs += 1

        if nbr2:

            num_bombs += 1

        if nbr3:

            num_bombs += 1

        if nbr4:

            num_bombs += 1

        if nbr5:

            num_bombs += 1

        if nbr6:

            num_bombs += 1

        if nbr7:

            num_bombs += 1

        if nbr8:

            num_bombs += 1

    return num_bombs
