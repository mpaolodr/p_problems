def variableName(name):

    try:

        first_char = int(name[0])
        return False

    except ValueError:

        pass

    allowed_symbol = "_"

    for char in name:

        if not char.isalnum() and char != allowed_symbol:

            return False

    return True
