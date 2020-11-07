def commonCharacterCount(s1, s2):

    s1_count = dict()
    s2_count = dict()

    for char in s1:

        if char not in s1_count:

            s1_count[char] = 0

        s1_count[char] += 1

    for char in s2:

        if char not in s2_count:

            s2_count[char] = 0

        s2_count[char] += 1

    common = set()

    for key in s1_count:

        if key in s2:

            common.add(key)

    if len(common) == 0:

        return 0

    count = 0

    for char in common:
        # print(char)
        # print(s1_count[char], s2_count[char])
        if s1_count[char] == s2_count[char]:

            count += s1_count[char]

        else:
            dif = abs(s1_count[char] - s2_count[char])

            count += s1_count[char] - \
                dif if s1_count[char] > s2_count[char] else s2_count[char] - dif

    return count
