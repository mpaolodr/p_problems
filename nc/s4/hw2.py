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
