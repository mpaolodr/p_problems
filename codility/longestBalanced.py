def solution(S):
    # write your code in Python 3.6
    uppercase = set()

    for char in S:

        if ord(char) < 97:

            uppercase.add(char)

    if len(uppercase) < 1:

        return -1

    i = 0
    max_len = 0

    while i < len(S):

        length = 0

        for j in range(i, len(S)):

            if S[j].upper() in uppercase:

                length += 1

            else:

                break

        max_len = max(max_len, length)

        i += 1

    return max_len if max_len > 1 else -1


print(solution("azABaabza"))
print(solution("TacoCat"))
print(solution("AcZCbaBz"))
