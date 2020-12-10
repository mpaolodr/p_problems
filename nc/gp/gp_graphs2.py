def flood_fill(image, sr, sc, new_color):

    # set the row length to the len of image
    rl = len(image)
    # set the col lenth to the len of image at 0 (because row may not be the same as col ie not a square matrix)
    cl = len(image[0])
    # extrapolate the color from the image at sr(starting row) and sc(starting column)
    color = image[sr][sc]
    # check if the color is the same as the new color
    if color == new_color:
        # return the image
        return image

    def dft(r, c):

        # check if the image at r and c is equal to color
        if image[r][c] == color:
            # set the image at r and c to the new color
            image[r][c] = new_color

            # do some recursive calls (get connections/neighbors)

            # if the r is >= 1
            if r >= 1:

                # call dft passing in r-1, c
                dft(r - 1, c)

            # if r + 1 is < row length
            if r + 1 < rl:

                # call dft passing in r+1, c
                dft(r + 1, c)

            # if c + 1 < col length
            if c + 1 < cl:

                # call dft passing in r, c + 1
                dft(r, c + 1)

    # do an initial call to dft passing in sr and sc
    dft(sr, sc)

    # return the image
    return image


test = flood_fill([
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
], 0, 0, 2)

print(test)
