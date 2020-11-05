def to_lower_case(string):
    # Your code here

    new_str = ""

    for char in string:

        if ord(char) < 97:

            char = chr(ord(char) + 32)

        new_str += char

    return new_str
