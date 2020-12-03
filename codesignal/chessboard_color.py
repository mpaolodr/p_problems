def chessBoardCellColor(cell1, cell2):

    e = ["w", "b", "w", "b", "w", "b", "w", "b"]
    o = ["b", "w", "b", "w", "b", "w", "b", "w"]

    table = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7
    }

    color_cell1 = e[table[cell1[0]]] if (
        int(cell1[1]) - 1) % 2 == 0 else o[table[cell1[0]]]
    color_cell2 = e[table[cell2[0]]] if (
        int(cell2[1]) - 1) % 2 == 0 else o[table[cell2[0]]]

    return color_cell1 == color_cell2
