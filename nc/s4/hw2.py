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


def csGroupAnagrams(strs):

    seen = set()

    results = list()

    for i in range(len(strs)):

        if strs[i] not in seen:

            res = [strs[i]] + get_nbrs(strs[i], strs[:i] + strs[i + 1:])

            for word in res:

                seen.add(word)

            results.append(res)

    return results


def get_nbrs(word, lst):

    checker = dict()
    nbrs = list()

    for c in word:

        if c not in checker:

            checker[c] = 0

        checker[c] += 1

    for word in lst:

        count = count_dict(word)
        valid_nbr = True

        for k in count:

            if k not in checker or checker[k] != count[k]:

                valid_nbr = False
                break

        if valid_nbr:

            nbrs.append(word)

    return nbrs


def count_dict(word):

    count = dict()

    for c in word:

        if c not in count:

            count[c] = 0

        count[c] += 1

    return count
