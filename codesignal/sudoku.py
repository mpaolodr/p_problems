def sudoku(grid):

    return check_col(grid) and check_row(grid) and check_square(grid)


def check_row(grid):

    for row in grid:

        tracker = set()

        for num in row:

            if num in tracker:

                return False

            tracker.add(num)

    return True


def check_col(grid):

    col = 0

    while col < len(grid):

        tracker = set()
        row = 0

        while row < len(grid):

            if grid[row][col] in tracker:

                return False

            tracker.add(grid[row][col])
            row += 1

        col += 1

    return True


def check_square(grid):

    for i in range(0, len(grid) - 2, 3):

        tracker = set()

        row = i

        while row < i + 3:

            for num in grid[row][i: i + 3]:

                if num in tracker:

                    return False

                tracker.add(num)

            row += 1

    return True
