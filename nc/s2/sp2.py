def reverseLinkedList(l):

    if l is None:

        return None

    if l.next is None:

        return l

    cur = l
    prev = None

    while cur is not None:

        if cur.next is None:

            l = cur

        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return l


def checkBlanagrams(word1, word2):

    diff1 = list()
    diff2 = list()

    for x, y in zip(word1, word2):

        if x != y:

            diff1.append(x)
            diff2.append(y)

    diff1_dict = {diff1[k]: diff1.count(diff1[k]) for k in range(len(diff1))}
    diff2_dict = {diff2[k]: diff2.count(diff2[k]) for k in range(len(diff2))}

    to_remove_1 = list()
    to_remove_2 = list()

    for k in diff1_dict:

        if k not in diff2_dict:

            to_remove_1.append(k)

        else:

            if diff1_dict[k] > diff2_dict[k] and diff1_dict[k] - diff2_dict[k] == 1:

                to_remove_1.append(k)

    for k in diff2_dict:

        if k not in diff1_dict:

            to_remove_2.append(k)

        else:

            if diff2_dict[k] > diff1_dict[k] and diff2_dict[k] - diff1_dict[k] == 1:

                to_remove_2.append(k)

    if len(to_remove_1) == 1 and len(to_remove_2) == 1:

        return True

    else:

        return False
