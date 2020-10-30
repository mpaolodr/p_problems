def addBorder(picture):

    max_len = max([len(c) for c in picture])

    with_border = [""] + picture + [""]

    for i in range(len(with_border)):

        if with_border[i] == "":

            with_border[i] = "*" + ("*" * max_len) + "*"

        else:

            with_border[i] = "*" + with_border[i] + "*"

    return with_border
