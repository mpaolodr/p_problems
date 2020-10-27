"""
Given a package with a weight limit limit and an array of integers items of where each integer represents the weight of
an item, implement a function merge_packages that finds the first two items in the items array whose sum of weights equals
the given weight limit limit.

Your function should return a pair [i, j] of the indices of the item weights, ordered such that i > j.
If such a pair doesn’t exist, return an empty array.
"""


def merge_packages(items, limit):

    test_dict = dict()
    possible_results = list()
    added_set = set()

    # create dictionary with item as key and value as list containing the item's index in items array

    for i in range(len(items)):

        if items[i] not in test_dict:

            test_dict[items[i]] = list()

        test_dict[items[i]].append(i)

    for key in test_dict:

        # limit - key is the other number we need from the list
        needed = limit - key

        # since we used each item as keys in our dictionary, search is O(1)
        if needed in test_dict:

            # if there's only one of this number in our list the list containing the indices will only be of length 1
            if len(test_dict[needed]) == 1:

                # we add pairs of indices, both in ascending and descending order, as tuples in a set to avoid duplicates
                # eg (0, 1) (1,0) will be avoided
                if (test_dict[needed][0], test_dict[key][0]) not in added_set and (test_dict[key][0], test_dict[needed][0]) not in added_set:

                    # we append to possible results list just in case there are multiple pairs that satisfies the condition
                    possible_results.append(
                        [test_dict[needed][0], test_dict[key][0]])

                    added_set.add((test_dict[needed][0], test_dict[key][0]))

            else:

                # if the pair of indices we want are the same number, we just need to return the value of key in our dictionary
                # it will contain the indices of the 2 numbers we want
                # instead of sorting, we just access by index so we stay at O(1)
                # return sorted(test_dict[key], reverse=True)
                return [test_dict[key][1], test_dict[key][0]]

    # if there are multiple indices that satisfies the condition...
    if len(possible_results) > 1:

        first_occuring = None

        # we loop instead of sorting so we stay at O(1)
        for item in possible_results:

            if first_occuring is None:

                first_occuring = item
                continue

            # we compare the larger index and see which one occured first
            if first_occuring[0] > item[0]:

                first_occuring = item

        return first_occuring

    else:

        return possible_results[0]

    return []


# tests
# items = [1, 2, 3]
# limit = 1
# items = [9]
# limit = 9
# items = [4, 6, 10, 15, 16]
# limit = 21

items = [4, 4, 4, 4]
limit = 8
# items = [1, 3, 7, 9]
# limit = 10
print(merge_packages(items, limit))
