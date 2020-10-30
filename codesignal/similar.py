def areSimilar(a, b):

    # we wanna make sure they have the same elements
    if len(set(a).union(set(b))) != len(set(a)):

        return False

    swaps = 0

    for i in range(len(b)):

        if a[i] != b[i]:

            swaps += 1

    if swaps <= 2 and sorted(a) == sorted(b):

        return True

    else:

        return False
