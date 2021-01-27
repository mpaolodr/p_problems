def chessKnight(cell):

    max_letter = ord("h")
    max_num = 8

    pos_res = generateHorizontal(cell, []) + generateVertical(cell, [])

    final_res = list()

    for char in pos_res:

        if (char[0].isalpha() and 97 <= ord(char[0]) < 105) and (char[1:].isnumeric() and 0 < int(char[1:]) <= 8):
            final_res.append(char)

    return len(final_res)


def generateHorizontal(position, moves_list):

    letter = position[0]
    num = int(position[1])

    # left
    first_l = chr(ord(letter) - 2) + str(num + 1)
    second_l = chr(ord(letter) - 2) + str(num - 1)

    # right
    first_r = chr(ord(letter) + 2) + str(num + 1)
    second_r = chr(ord(letter) + 2) + str(num - 1)

    moves_list.append(first_l)
    moves_list.append(first_r)
    moves_list.append(second_l)
    moves_list.append(second_r)

    return moves_list


def generateVertical(position, moves_list):

    letter = position[0]
    num = int(position[1])

    # top
    first_t = chr(ord(letter) - 1) + str(num + 2)
    second_t = chr(ord(letter) + 1) + str(num + 2)

    # bottom
    first_b = chr(ord(letter) - 1) + str(num - 2)
    second_b = chr(ord(letter) + 1) + str(num - 2)

    moves_list.append(first_t)
    moves_list.append(first_b)
    moves_list.append(second_t)
    moves_list.append(second_b)

    return moves_list
