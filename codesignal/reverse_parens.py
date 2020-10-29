def reverseInParentheses(inputString):

    if len(inputString) < 2:

        return inputString

    string_copy = inputString
    parens_pos = parens_position(string_copy)

    while len(parens_pos) > 0:

        eval_pair = parens_pos.pop(0)

        string_to_replace = string_copy[eval_pair[0]: eval_pair[1] + 1]
        evaluated_string = string_copy[eval_pair[0] + 1: eval_pair[1]][::-1]

        # replace
        string_copy = string_copy.replace(string_to_replace, evaluated_string)

        parens_pos = parens_position(string_copy)

    return string_copy


def parens_position(inputString):

    position = list()
    parens_stack = list()

    for i, val in enumerate(inputString):

        if val == "(":

            parens_stack.append(i)

        elif val == ")":

            opening = parens_stack.pop()
            position.append((opening, i))

    return position
