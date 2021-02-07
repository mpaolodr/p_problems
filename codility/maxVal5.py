

def solution(N):
    # write your code in Python 3.6\

    max_possible = None

    # convert to string so we can loop through it
    to_string = list(str(N))

    i = 0

    if to_string[0] == "-":

        i = 1

    while i < len(to_string):

        before_string = to_string[::]
        after_string = to_string[::]

        before_string.insert(i, "5")
        after_string.insert(i + 1, "5")

        before_num = int("".join(before_string))
        after_num = int("".join(after_string))

        if max_possible is None:

            max_possible = max(before_num, after_num)

        else:

            max_possible = max(max_possible, max(before_num, after_num))

        i += 1

    if to_string[0] == "-":

        return 1 * max_possible

    return max_possible


print(solution(268))
print(solution(670))
print(solution(0))
print(solution(-999))
