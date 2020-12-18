def csIsomorphicStrings(a, b):

    a_dic = dict()
    b_dic = dict()

    for char in a:

        if char not in a_dic:

            a_dic[char] = 0

        a_dic[char] += 1

    for char in b:

        if char not in b_dic:

            b_dic[char] = 0

        b_dic[char] += 1

    if len(a) != len(b):

        return False

    for x, y in zip(a_dic, b_dic):

        if a_dic[x] != b_dic[y]:

            return False

    return True


def csWordPattern(pattern, a):

    split_words = a.split()

    if len(pattern) != len(split_words):

        return False

    mapper = dict()
    seen = set()

    for char, word in zip(pattern, split_words):

        if char not in mapper:

            mapper[char] = ""

        if mapper[char] == "" and word not in seen:

            seen.add(word)
            mapper[char] = word

    i = 0
    j = 0

    while i < len(pattern):

        if mapper[pattern[i]] != split_words[j]:

            return False

        i += 1
        j += 1

    return True
