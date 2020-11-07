def sortByHeight(a):

    for i in range(len(a) - 1):

        smallest_index = i

        if a[i] > 0:

            for j in range(i + 1, len(a)):

                next_num = a[j]

                if next_num > 0:

                    if a[smallest_index] > next_num:

                        smallest_index = j

            a[smallest_index], a[i] = a[i], a[smallest_index]

    return a
