def boxBlur(image):

    columns = list()
    max_row = 0

    for i in range(len(image)):

        if i + 3 > len(image):

            break

        max_row = i + 1

    j = 0

    while j + 2 < len(image[0]):

        start = j
        mid = j + 1
        end = j + 2

        columns.append([start, mid, end])

        j += 1

    results = list()
    cur_row = 0

    while cur_row < max_row:

        temp = list()

        for i in range(len(columns)):

            total = 0

            for col in columns[i]:

                first = image[cur_row][col]
                second = image[cur_row + 1][col]
                third = image[cur_row + 2][col]

                total += (first + second + third)

            temp.append(total // 9)

        results.append(temp)
        cur_row += 1

    return results
