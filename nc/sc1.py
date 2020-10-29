def removeAdjacent(s):

    to_list = list(s)  # O(n)

    for i in range(len(to_list) - 1, 0, -1):  # O(n)

        if to_list[i - 1] == to_list[i]:  # O(1)

            del to_list[i - 1]  # O(n)

    return "".join(to_list)  # O(n)


def reverse_String(input):

    start = 0
    last = len(input) - 1

    while start < last:

        input[start], input[last] = input[last], input[start]

        start += 1
        last -= 1

    return input
