def messageFromBinaryCode(code):

    result = ""
    for i in range(0, len(code), 8):

        result += chr(int(code[i: i + 8], base=2))

    return result
