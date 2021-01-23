def lineEncoding(s):

    char_count = list()

    current = s[0]
    current_count = 1

    result = ""

    for i in range(1, len(s)):

        if s[i] == current:

            current_count += 1

        else:

            if current_count > 1:

                result += f"{current_count}{current}"

            else:

                result += current

            current = s[i]
            current_count = 1

        if i == len(s) - 1:

            if current_count > 1:

                result += f"{current_count}{current}"

            else:

                result += current

    return result
